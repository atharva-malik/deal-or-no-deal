from flask import Flask, render_template, request, redirect # ! pip install flask
import os, json, csv
# * FUNCTIONS IMPORTS
#import random, time, getpass, os, json
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #* This is to hide the pygame welcome message
from pygame import mixer #! pip install pygame
from passwords_module import password_management

app = Flask(__name__)


# * FUNCTIONS START HERE

def f_list_to_string(list):
    #* This function converts a list to a string. It is used with the remaining briefcases
    #* It works by adding each element of the list to a string and adding a space after each element
    string = ""
    for i in list:
        string += i + " "
    return string


def f_makePlayers(number):
    #* This function makes a dictionary with the keys being the player numbers and the values being the player's money
    players = {}
    for i in range(1, number+1):
        players[str(i)] = 0
    return players


def f_get_offer(briefcases):
    #* The offer in the Deal or No Deal show is calculated using this formula:
    #* sqrt(sum of all briefcases^2 / number of briefcases)
    #* This function uses the same formula to calculate the offer
    sumSqr = 0
    for i in briefcases.values():
        sumSqr += i**2
    offer = sumSqr / len(briefcases)
    offer = offer**0.5
    offer = round(offer, 2)
    return offer


def f_init_briefcases():
    #* This function initialises the briefcases with random amounts of money using the random module
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
              750000, 1000000]
    for i in range(1, 27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
    return briefcases


def f_change_setting():
    #* Changes the setting of the game
    setting_path = os.path.dirname(__file__).replace("\\deal_no_deal_module", "") + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "r") as f:
        for setting in f.readlines():
            settings.append(setting.strip("\n"))    
    if settings[0] == "yes music":
        #* Changes the settings file if your setting is to have music on
        settings = ["no music"]
        print(magenta("Turned the background music off."))
        with open(setting_path, "w") as f:
            f.writelines(settings)
        return "no_music"
    elif settings[0] == "no music":
        #* Changes the settings file if your setting is to have music on
        settings = ["yes music"]
        print(magenta("Turned the background music on."))
        with open(setting_path, "w") as f:
            f.writelines(settings)
        return "music"


def f_check_setting():
    #* Checks the settings of the game
    #* This is used to check whether to play music or not
    setting_path = os.path.dirname(__file__).replace("\\deal_no_deal_module", "") + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "r") as f:
        for setting in f.readlines():
            settings.append(setting.strip("\n"))    
    if settings[0] == "yes music":
        return "music"
    elif settings[0] == "no music":
        return "no_music"


def f_mtutorial():
    #* This function is the tutorial for the multiplayer mode
    print(green("This game mode is the same other than the following rules:\nYou take turns, eliminating one briefcase each\n"\
                "The goal is to be the one with the most money\nAnd, lastly you will be given the option to take the same deal as the player before you\n"\
                "\nNow let's play a multiplayer round."))
    #* This ensures that the user enters a valid number of players
    while True:
        try:
            numberOfPlayers = int(input("Enter a number between 2 and 4: "))
            if numberOfPlayers < 2 or numberOfPlayers > 4:
                continue
            break
        except Exception:
            continue
    multiplayer(numberOfPlayers)


def f_gameOver(players):
    #* This function checks if the game is over
    ret = False
    won = 0
    for player in players:
        if players[player] != 0:
            won += 1
    if won == len(players):
        ret = True
    return ret


def f_multiplayer(numberOfPlayers):
    #* This is the main function for the multiplayer mode and works slightly differently to the single player mode
    #* Initialise all the variables
    briefcases = init_briefcases()
    players = makePlayers(numberOfPlayers) #* This creates a dictionary of players to keep track of their earnings
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    remaining_briefcases_for_display = [blue(1, "bold"), blue(2, "bold"), blue(3, "bold"), blue(4, "bold"), blue(5, "bold"), 
                                        blue(6, "bold"), blue(7, "bold"), blue(8, "bold"), blue(9, "bold"), blue(10, "bold"), 
                                        blue(11, "bold"), blue(12, "bold"), blue(13, "bold"), blue(14, "bold"), blue(15, "bold"),
                                        blue(16, "bold"), blue(17, "bold"), blue(18, "bold"), blue(19, "bold"), blue(20, "bold"),
                                        blue(21, "bold"), blue(22, "bold"), blue(23, "bold"), blue(24, "bold"), blue(25, "bold"), blue(26, "bold")]
    remaining_money_for_display =       [blue(0.1, "bold"), blue(1, "bold"), blue(5, "bold"), blue(10, "bold"), blue(25, "bold"), 
                                        blue(50, "bold"), blue(75, "bold"), blue(100, "bold"), blue(200, "bold"), blue(300, "bold"), 
                                        blue(400, "bold"), blue(500, "bold"), blue(750, "bold"), blue(1000, "bold"), blue(5000, "bold"),
                                        blue(10000, "bold"), blue(25000, "bold"), blue(50000, "bold"), blue(75000, "bold"), blue(100000, "bold"),
                                        blue(200000, "bold"), blue(300000, "bold"), blue(400000, "bold"), blue(500000, "bold"), 
                                        blue(750000, "bold"), blue(1000000, "bold")]
    briefcases_to_eliminate = 1

    #* Makes both player eliminate one briefcases each
    for player in players:
        print(yellow("Player " + player + "'s turn!", ["bold", "italic"])) #* Tells the user which player's turn it is
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display),"Pick", briefcases_to_eliminate, "that you will discard.")
        #* Checks to see if the user has entered a valid number
        while True:
            try:
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                break
            except Exception:
                continue
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        #* Removes the briefcase from the list of remaining briefcases and updates the display
        remaining_briefcases.remove(number_to_eliminate)
        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
        time.sleep(3)
        os.system("cls") #* Clears the screen to make it look cleaner

    while briefcases_to_eliminate >= 1:
        #* Check to see if the game is over
        if gameOver(players):
            print(cyan("Good game players!. At the end the winner is: ", "bold"))
            print(cyan(dict(sorted(players.items(), key=lambda x:x[1], reverse=True)), "bold"))
            break
        for player in players:
            #* Check to see if the player has won some money
            if players[player] == 0:
                os.system("cls")
                print(yellow("Player " + player + "'s turn!", ["bold", "italic"]))
                offer = get_offer(briefcases)
                print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
                choice = input("[D]eal or [N]o Deal? ")
                #* Allows the user to view the offer and choose to take it
                if choice.lower() == "d":
                    os.system("cls")
                    #* Stops the game and congratulates the user for accepting the offer
                    print("Good game Player", player, "! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
                    choice = "n"
                    numberOfPlayers -= 1
                    players[player] = offer
                elif choice.lower() == "n":
                    os.system("cls")
                    #* If there is only one briefcase left, the user must take it
                    if len(remaining_briefcases) == 1:
                        print("You have one briefcase left. You must take it.")
                        offer = briefcases.pop(str(remaining_briefcases[0]))
                        print("You won $", offer, "!")
                        players[player] = offer
                        if not gameOver(players): #* Checks to see if there is only more than one player left
                            print(cyan("Good game players!. At the end the winner is: ", "bold"))
                            print(cyan(dict(sorted(players.items(), key=lambda x:x[1], reverse=True)), "bold"))
                            break
                    elif briefcases_to_eliminate == 1:
                        #* Runs the standard logic from the for loop above
                        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                        while True:
                            try:
                                number_to_eliminate = int(input("Briefcase to eliminate: "))
                                money = briefcases[str(number_to_eliminate)]
                                break
                            except Exception:
                                continue
                        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                        remaining_briefcases.remove(number_to_eliminate)
                        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
                else:
                    #* If the input is incorrect, the loop restarts
                    continue
#* FUNCTIONS END HERE
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


# * Used for the highscores
def f_add_float_in_descending_order(numbers, new_number):
    # * Convert the strings to floats, and add the new float
    numbers = [float(n) for n in numbers] + [new_number]
    # * Sort the list in descending order
    numbers = sorted(numbers, reverse=True)
    # * Truncate the list to 10 elements if necessary
    if len(numbers) > 10:
        numbers = numbers[:10]
    # * Convert the floats back to strings and return the result
    return [str(n) + "\n" for n in numbers]


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
    return render_template("game.html")


@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")


@app.route("/multiplayer-tutorial")
def multiplayer_tutorial():
    return render_template("multiplayer-tutorial.html")


@app.route("/multiplayer/<int:players>")
def multiplayer(players):
    return render_template("multiplayer.html", players=players)


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
