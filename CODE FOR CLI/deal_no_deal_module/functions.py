import random, time, getpass, os, json, keyboard #! pip install keyboard
from simple_colors import * #! pip install simple_colors
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #* This is to hide the pygame welcome message
from pygame import mixer #! pip install pygame
from deal_no_deal_module.passwords_module import password_management


mixer.init() #* This is to initialise the mixer
audio_file = os.path.dirname(__file__) + '\\background.mp3'
mixer.music.load(audio_file) #* This is to load the background music and prepare to play/stop it

def list_to_string(list):
    #* This function converts a list to a string. It is used with the remaining briefcases
    #* It works by adding each element of the list to a string and adding a space after each element
    string = ""
    for i in list:
        string += i + " "
    return string


def makePlayers(number):
    #* This function makes a dictionary with the keys being the player numbers and the values being the player's money
    players = {}
    for i in range(1, number+1):
        players[str(i)] = 0
    return players


def play_background_music():
    #* This functions simply starts the song and sets the number of repeats to infinite
    mixer.music.play(loops=-1)


def stop_background_music():
    #* This function simply stops the song
    mixer.music.stop()


def get_offer(briefcases):
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


def init_briefcases():
    #* This function initialises the briefcases with random amounts of money using the random module
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
              750000, 1000000]
    for i in range(1, 27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
    return briefcases


def deal_or_no_deal():
    #* This is the main function!
    #* Initialise all the variables
    briefcases = init_briefcases()
    offer = 0
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
    briefcases_to_eliminate = 6

    #* Starts the first sequence as you have no choice other than to eliminate 6 briefcases
    #* as your first move
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        #* This part prints the briefcases left and the amounts of money left to allow strategic decision making
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display),"\nPick", briefcases_to_eliminate, "that you will discard.")
        #* This section ensures that the user picks a valid briefcases
        while True:
            try:
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                break
            except Exception:
                continue
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        #* Removes the briefcase that the user has eliminated from the list of briefcases and changes the color of the briefcase and money to black
        remaining_briefcases.remove(number_to_eliminate)
        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
        time.sleep(3)
        os.system("cls") #* Clears the screen to make it look cleaner
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and make a strategic decision
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting the offer
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            return offer
        elif choice.lower() == "n":
            os.system("cls")
            #* If there is only one briefcase, the user must take it
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                offer = briefcases.pop(str(remaining_briefcases[0]))
                print("You won $", offer, "!")
                return offer
            #* If he has to eliminate only one briefcase, no point in running the for loop
            elif briefcases_to_eliminate == 1:
                #* The internal logic stays the same as the first for loop
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
            #* Otherwise there are more than one briefcases to eliminate and the for loop runs
            else:
                #* The internal logic stays the same as the first for loop
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
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
                    time.sleep(3)
                    os.system("cls")
                briefcases_to_eliminate -= 1
        else:
            #* If the input is incorrect, the loop restarts
            continue


def change_setting():
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


def check_setting():
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


def tutorial():
    #* Initialise all the variables
    briefcases = init_briefcases()
    offer = 0
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
    briefcases_to_eliminate = 6

    #* Starts the first sequence as you have no choice other than to eliminate 6 briefcases
    #* as your first move
    print(green("The game starts and there are 26 briefcases. To start with you eliminate 6 briefcases," \
                "this number progressively goes down if you don't make a deal.\n" \
                "The money in the briefcases is removed from the prize pool."))
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        #* This part prints the briefcases left and the amounts of money left to allow strategic decision making
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display),"Pick", briefcases_to_eliminate, "that you will discard.")
        #* This section ensures that the user picks a valid briefcases
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
        time.sleep(3)
        os.system("cls") #* Clears the screen to make it look cleaner
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    print(green("Now you will be offered a deal. If you accept, the game ends and you leave with the amount you were offered.\n" \
                "If you decline the game continues"))
    time.sleep(2)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and make a strategic decision
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting the offer
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
            os.system("cls")
            #* If there is only one briefcase, the user must take it
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                print("You won $", briefcases.pop(str(remaining_briefcases[0])), "!")
                break
            #* If he has to eliminate only one briefcase, no point in running the for loop
            elif briefcases_to_eliminate == 1:
                #* The internal logic stays the same as the first for loop
                print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                while True:
                    try:
                        number_to_eliminate = int(input("Briefcase to eliminate: "))
                        money = briefcases[str(number_to_eliminate)]
                        break
                    except Exception:
                        continue
                money = briefcases[str(number_to_eliminate)]
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
                remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            #* Otherwise there are more than one briefcases to eliminate and the for loop runs
            else:
                #* The internal logic stays the same as the first for loop
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
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
                    time.sleep(3)
                    os.system("cls")
                briefcases_to_eliminate -= 1
        else:
            #* If the input is incorrect, the loop restarts
            continue


def login():
    #* This function allows the user to login
    while True: #* This loop ensures that the user enters a valid username
        username = input("Username: ")
        users = json.load(open("users.json", "r"))
        if username not in users:
            print(red("Wrong username!", "bold"))
            time.sleep(1)
            os.system("cls")
        else:
            password = getpass.getpass("Password: ") #* This is used to hide the password
            correct_password = password_management.retrieve_password(username) #* This is decrypted and taken from the users.json file
            if password == correct_password:
                print(green("Login Success!", "bold"))
                time.sleep(1)
                os.system("cls")
                return username #* This is returned so that the username can be used in the main function
            else:
                print(red("Wrong password!", "bold")) #* If the password is incorrect, the loop restarts
                time.sleep(1)
                os.system("cls")


def signup():
    #* This function allows the user to create an account
    username = input("Username: ")
    if username in json.load(open("users.json", "r")): #* This checks if the username already exists
        print(red("Username already exists!", "bold"))
        return
    password = getpass.getpass("Password: ") #* This is used to hide the password
    password, key = password_management.encrypt_password(password) #* This is encrypted and stored in the users.json file
    password_management.store_password(password, key, username)
    print(green("Account created!", "bold"))


def login_or_signup():
    #* This function allows the user to login or signup
    print("Press L to login or S to signup")
    while True:
        if keyboard.is_pressed("l"):
            keyboard.press("backspace")
            username = login()
            break
        elif keyboard.is_pressed("s"):
            keyboard.press("backspace")
            signup()
            print("Login")
            username = login()
            break
    return username


def mtutorial():
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


def gameOver(players):
    #* This function checks if the game is over
    ret = False
    won = 0
    for player in players:
        if players[player] != 0:
            won += 1
    if won == len(players):
        ret = True
    return ret


def multiplayer(numberOfPlayers):
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