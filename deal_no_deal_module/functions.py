import random
import _thread
from playsound import playsound
import time
import os
from simple_colors import *


def play_background_music():
    audio_file = os.path.dirname(__file__) + '\\experiments\\KomuramBheemudo.mp3'
    playsound(audio_file)


def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases) #TODO: Try to make this more exciting
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
    briefcases_to_eliminate = 6

    #* Starts the first sequence as you have no choice other than to eliminate 6 briefcases
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
        time.sleep(3)
        os.system("cls")
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and choose to take it
        offer = get_offer(briefcases)
        print("Remaining briefcases:", len(remaining_briefcases), remaining_briefcases, "Offer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
            os.system("cls")
            #* Checks how many briefcases are left and runs the correct version
            if briefcases_to_eliminate == 1 and len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                print("You won $", briefcases.pop(str(remaining_briefcases[0])), "!")
                break
            elif briefcases_to_eliminate == 1:
                print("There are", len(remaining_briefcases), "briefcases left. Pick which one you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
            else:
                print("There are", len(remaining_briefcases), "briefcases left. Pick", briefcases_to_eliminate, "that you will discard.")
                for i in range(0, briefcases_to_eliminate):
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                    remaining_briefcases.remove(number_to_eliminate)
                    time.sleep(3)
                    os.system("cls")
                briefcases_to_eliminate -= 1
        else:
            #* If the input is incorrect, the loop restarts
            continue


def change_setting():
    setting_path = os.path.dirname(__file__).replace("\\deal_no_deal_module", "") + "\\deal_no_deal.settings"
    with open(setting_path, "w") as f:
        f.write("yesMusic\n")
        f.write("yesSfx")

def change_setting():
    setting_path = os.path.dirname(__file__).replace("\\deal_no_deal_module", "") + "\\deal_no_deal.settings"
    settings = []
    with open(setting_path, "r") as f:
        for setting in f.readlines():
            settings.append(setting.strip("\n"))
    setting_to_toggle = input("The current settings are: " + str(settings[0]).capitalize() + ", " + str(settings[1]).capitalize() + ". \nEnter setting name to toggle: ")
    if "music" in setting_to_toggle.lower():
        if settings[0] == "yes music":
            settings = ["no music", "\n", settings[1]]
        elif settings[0] == "no music":
            settings = ["yes music", "\n", settings[1]]
    elif "sfx" in setting_to_toggle.lower():
        if settings[1] == "yes sfx":
            settings = [settings[0], "\n", "no sfx"]
        elif settings[1] == "no sfx":
            settings = [settings[0], "\n", "yes sfx"]
    else:
        print(red("Wrong Input! Redirecting you to home!", "bold"))
    with open(setting_path, "w") as f:
        f.writelines(settings)
change_setting()


def tutorial():
    #* Initialise all the variables
    briefcases = init_briefcases()
    offer = 0
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    briefcases_to_eliminate = 6

    #* Starts the first sequence as you have no choice other than to eliminate 6 briefcases
    print(green("""The game starts and there are 26 briefcases. To start with you eliminate 6 briefcases, this number progressively goes down if you don't make a deal.
The money in the briefcases is removed from the prize pool."""))
    for i in range(0, briefcases_to_eliminate): #* This statement runs the code, allowing the user to eliminate the number you need to
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
        time.sleep(3)
        os.system("cls")
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    print(green("""Now you will be offered a deal. If you accept, the game ends and you leave with the amount you were offered.
If you decline the game continues"""))
    time.sleep(2)
    
    #* Starts the loop that allows the user to choose [D]eal or [N]o Deal
    while briefcases_to_eliminate >= 1:
        #* Allows the user to view the offer and choose to take it
        offer = get_offer(briefcases)
        print("Remaining briefcases:", len(remaining_briefcases), remaining_briefcases, "Offer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [N]o Deal? ")
        if choice.lower() == "d":
            os.system("cls")
            #* Stops the game and congratulates the user for accepting it
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
            os.system("cls")
            #* Checks how many briefcases are left and runs the correct version
            if briefcases_to_eliminate == 1 and len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                print("You won $", briefcases.pop(str(remaining_briefcases[0])), "!")
                break
            elif briefcases_to_eliminate == 1:
                print("There are", len(remaining_briefcases), "briefcases left. Pick which one you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
            else:
                print("There are", len(remaining_briefcases), "briefcases left. Pick", briefcases_to_eliminate, "that you will discard.")
                for i in range(0, briefcases_to_eliminate):
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                    remaining_briefcases.remove(number_to_eliminate)
                    time.sleep(3)
                    os.system("cls")
                briefcases_to_eliminate -= 1
        else:
            #* If the input is incorrect, the loop restarts
            continue
