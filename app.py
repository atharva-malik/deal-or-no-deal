from flask import Flask, render_template, request, redirect # ! pip install flask
import os, json, csv
# * FUNCTIONS IMPORTS
#import random, time, getpass, os, json
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #* This is to hide the pygame welcome message
from pygame import mixer #! pip install pygame
from passwords_module import password_management

app = Flask(__name__)

#* Global variables
loggedInUser = ""
soundLevel = 1
musicOnOff = "on"


def getSettings():
    global soundLevel
    global musicOnOff
    #* This is used to check whether to play music or not
    setting_path = os.path.dirname(__file__) + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "r") as f:
        for setting in f.readlines():
            settings.append(setting.strip("\n"))    
    if settings[0] == "yes music":
        musicOnOff = "on"
    elif settings[0] == "no music":
        musicOnOff = "off"
    soundLevel = float(settings[1])
getSettings()


def setSettings():
    global soundLevel
    global musicOnOff
    #* This is used to check whether to play music or not
    setting_path = os.path.dirname(__file__) + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "w") as f:
        if musicOnOff == "on":
            f.write("yes music\n")
        elif musicOnOff == "off":
            f.write("no music\n")
        f.write(str(soundLevel))


def insertIntoHighs(acceptedOffer):
    global loggedInUser
    #* Get list of scores 
    scores = []
    users = []
    with open('highscores.csv', 'r') as file:
        #* Create a reader object
        reader = csv.reader(file)
        #* Iterate over the rows in the reader object and extract the values from the desired columns
        for row in reader:
            scores.append(row[0])
            users.append(row[1])
    #* Insert scores
    index = 0
    if float(acceptedOffer) < float(scores[-1]):
        return "" #* This means it is the lowest number on the sorted list
    for score in scores:
        if float(acceptedOffer) >= float(score):
            break
        index+=1
    scores.remove(scores[-1])
    users.remove(users[-1])
    scores.insert(index, acceptedOffer)
    users.insert(index, loggedInUser)
    print(scores, users)
    #* Output to file
    with open('highscores.csv', 'w') as file:
        index = 0
        for i in scores:
            file.write(i + ", " + users[index])
            file.write("\n")
            index+=1
        file.close()
    return ""

@app.route("/process_value", methods=["POST"])
def process_value():
    #* As this handles the communications for the whole network, it contains multiple try 
    #* and excepts to see what value it's receiving.
    global soundLevel
    global musicOnOff
    try:
        acceptedOffer = request.form["value"]
        insertIntoHighs(acceptedOffer)
    except Exception as e:
        print(e)
    try:
        soundLevel = int(request.form["volume"])/100
    except Exception as e:
        print(e)
    try:
        value = request.form["backgroundmusic"]
        if value == "":
            musicOnOff = "on"
        elif value == "null":
            musicOnOff = "off"
    except Exception as e:
        print(e)
    setSettings()
    return ""


@app.route("/")
def home():
    global loggedInUser
    if loggedInUser != "":
        return redirect("/home")
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    global loggedInUser
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = json.load(open("users.json", "r"))
        if password == "" and username == "":
            error = "noPasswordOrUsername"
        elif password == "":
            error = "noPassword"
        elif username == "":
            error = "noUsername"
        elif username not in users:
            error = "wrongUsername"
        else:
            correct_password = password_management.retrieve_password(username) #* This is decrypted and taken from the users.json file
            if password == correct_password:
                loggedInUser = username
                return redirect("/home")
            else:
                error = "wrongPassword"
    return render_template('login.html', message=error)


@app.route("/game/<username>")
def loggedInGame(username):
    global musicOnOff
    global soundLevel
    global loggedInUser
    if loggedInUser == "":
        return redirect("/login")
    return render_template("loggedingame.html", musicOnOff=musicOnOff, sound_level=soundLevel)


@app.route("/logout")
def logout():
    global loggedInUser
    loggedInUser = ""
    return redirect("/")#todo: fixme


@app.route("/home")
def user_home():
    global loggedInUser
    if loggedInUser == "":
        return redirect("/login")
    return render_template("userhome.html", username=loggedInUser)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "" and password == "":
            error = "noPasswordAndUsername"
        elif username == "":
            error = "noUsername"
        elif password == "":
            error = "noPassword"
        #* This function allows the user to create an account
        elif username in json.load(open("users.json", "r")): #* This checks if the username already exists
            error = "usernameExists"
        else:
            password, key = password_management.encrypt_password(password) #* This is encrypted and stored in the users.json file
            password_management.store_password(password, key, username)
            return redirect('/login')
    return render_template('signup.html', message=error)


@app.route("/game")
def game():
    global musicOnOff
    global soundLevel
    global loggedInUser
    if loggedInUser != "":
        return redirect(f"/game/{loggedInUser}")
    return render_template("game.html", musicOnOff=musicOnOff, sound_level=soundLevel)


@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")


@app.route("/multiplayer-tutorial")
def multiplayer_tutorial():
    return render_template("multiplayer-tutorial.html")


@app.route("/multiplayer/<int:players>")
def multiplayer(players):
    global musicOnOff
    global soundLevel
    return render_template("multiplayer.html", players=players, musicOnOff=musicOnOff, sound_level=soundLevel)


@app.route("/multiInit", methods=["GET", "POST"])
def mInit():
    error = ""
    if request.method == "POST":
        numberOfPlayers = request.form['players']
        try:
            numberOfPlayers = int(numberOfPlayers)
            if numberOfPlayers > 4 or numberOfPlayers < 2:
                error = "between42"
            else:
                return redirect(f"/multiplayer/{numberOfPlayers}")
        except Exception:
            error = "notInt"
    return render_template("mInit.html", error=error)


@app.route("/highscores")
def highscores():
    users = []
    scores = []
    with open('highscores.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        #header = next(csvreader)
        for row in csvreader:
            scores.append(float(row[0]))
            users.append(row[1])
    print(users, scores)
    return render_template("highscores.html", scores=scores, users=users)


@app.route("/settings")
def settings():
    global musicOnOff
    global soundLevel
    return render_template("settings.html", musicOnOff=musicOnOff, soundLevel=soundLevel)


if __name__ == "__main__":
    app.run(debug=True)
