import random, time, getpass, os, json, keyboard
from playsound import playsound
from simple_colors import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
from deal_no_deal_module.passwords_module import password_management


mixer.init()
audio_file = os.path.dirname(__file__).replace("deal_no_deal_module", "") + '\\lofi.mp3'
mixer.music.load(audio_file)

def list_to_string(list):
    string = ""
    for i in list:
        string += i + " "
    return string


def makePlayers(number):
    players = []
    for i in range(1, number+1):
        players.append(str(i))
    return players


def play_background_music():
    mixer.music.play(loops=-1)


def stop_background_music():
    mixer.music.stop()


def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases) #TODO: Try to make this more exciting
    offer = round(offer, 2)
    return offer


def init_briefcases():
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
              750000, 1000000]
    for i in range(1, 27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
    return briefcases


def deal_or_no_deal():
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
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money is", list_to_string(remaining_money_for_display),"\nPick", briefcases_to_eliminate, "that you will discard.")
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        money = briefcases[str(number_to_eliminate)]
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
        time.sleep(3)
        os.system("cls")
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and choose to take it
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money:", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            return offer
        elif choice.lower() == "n":
            os.system("cls")
            #* Checks how many briefcases are left and runs the correct version
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                offer = briefcases.pop(str(remaining_briefcases[0]))
                print("You won $", offer, "!")
                return offer
            elif briefcases_to_eliminate == 1:
                print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
                remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            else:
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    money = briefcases[str(number_to_eliminate)]
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
    setting_path = os.path.dirname(__file__).replace("\\deal_no_deal_module", "") + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "r") as f:
        for setting in f.readlines():
            settings.append(setting.strip("\n"))    
    if settings[0] == "yes music":
        settings = ["no music"]
        print(magenta("Turned the background music off."))
        with open(setting_path, "w") as f:
            f.writelines(settings)
        return "no_music"
    elif settings[0] == "no music":
        settings = ["yes music"]
        print(magenta("Turned the background music on."))
        with open(setting_path, "w") as f:
            f.writelines(settings)
        return "music"


def check_setting():
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
    print(green("The game starts and there are 26 briefcases. To start with you eliminate 6 briefcases," \
                "this number progressively goes down if you don't make a deal.\n" \
                "The money in the briefcases is removed from the prize pool."))
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money is", list_to_string(remaining_money_for_display),"\nPick", briefcases_to_eliminate, "that you will discard.")
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        money = briefcases[str(number_to_eliminate)]
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
        time.sleep(3)
        os.system("cls")
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    print(green("Now you will be offered a deal. If you accept, the game ends and you leave with the amount you were offered.\n" \
                "If you decline the game continues"))
    time.sleep(2)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and choose to take it
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money:", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
            os.system("cls")
            #* Checks how many briefcases are left and runs the correct version
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                print("You won $", briefcases.pop(str(remaining_briefcases[0])), "!")
                break
            elif briefcases_to_eliminate == 1:
                print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
                remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            else:
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    money = briefcases[str(number_to_eliminate)]
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
    while True:
        username = input("Username: ")
        users = json.load(open("users.json", "r"))
        if username not in users:
            print(red("Wrong username!", "bold"))
            time.sleep(1)
            os.system("cls")
        else:
            password = getpass.getpass("Password: ")
            correct_password = password_management.retrieve_password(username)
            if password == correct_password:
                print(green("Login Success!", "bold"))
                time.sleep(1)
                os.system("cls")
                return username
            else:
                print(red("Wrong password!", "bold"))
                time.sleep(1)
                os.system("cls")


def signup():
    username = input("Username: ")
    if username in json.load(open("users.json", "r")):
        print(red("Username already exists!", "bold"))
        return
    password = getpass.getpass("Password: ")
    password, key = password_management.encrypt_password(password)
    password_management.store_password(password, key, username)
    print(green("Account created!", "bold"))


def login_or_signup():
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
    pass


def multiplayer(number):
    #* Initialise all the variables
    briefcases = init_briefcases()
    players = makePlayers(number)
    offerP1 = 0
    offerP2 = 0
    turn = 1
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
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for player in players:
        print(yellow("Player " + player + "'s turn!", ["bold", "italic"]))
        for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
            print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money is", list_to_string(remaining_money_for_display),"\nPick", briefcases_to_eliminate, "that you will discard.")
            number_to_eliminate = int(input("Briefcase to eliminate: "))
            money = briefcases[str(number_to_eliminate)]
            print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
            remaining_briefcases.remove(number_to_eliminate)
            remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
            remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            time.sleep(3)
            os.system("cls")
        
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money:", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game Player", g, "! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
        elif choice.lower() == "n":
            os.system("cls")
        
        #region  Should not be needed as the next part does it
        """
            #* Checks how many briefcases are left and runs the correct version
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                offer = briefcases.pop(str(remaining_briefcases[0]))
                print("You won $", offer, "!")
                return offer
            elif briefcases_to_eliminate == 1:
                print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
                remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            else:
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    money = briefcases[str(number_to_eliminate)]
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
        briefcases_to_eliminate -= 1
        offer = get_offer(briefcases)
        """
        #endregion
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and choose to take it
        offer = get_offer(briefcases)
        print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money:", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            return offer
        elif choice.lower() == "n":
            os.system("cls")
            #* Checks how many briefcases are left and runs the correct version
            if len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                offer = briefcases.pop(str(remaining_briefcases[0]))
                print("You won $", offer, "!")
                return offer
            elif briefcases_to_eliminate == 1:
                print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
                remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
            else:
                for i in range(0, briefcases_to_eliminate):
                    print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is: ", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    money = briefcases[str(number_to_eliminate)]
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
