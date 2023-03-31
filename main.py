from deal_no_deal_module import functions
from simple_colors import * #! pip install simple_colors

def cli(command):
    if command.lower() == "help":
        print("""[HELP]: Displays this
[EXIT]: To quit the app
[L]ogin: Allows user login
[Tutorial]: Runs the game in tutorial mode
[G]uest: To play as guest
[2] player: Runs game in 2 player mode
[3] player: Runs game in 3 player mode
[4] player: Runs game in 3 player mode
[H]ighscore: Shows the list of high scores
[S]ettings: Allows user to change the settings""") # TODO add list of commands
    elif command.lower() == "l": #todo add the login function
        pass
    elif command.lower() == "g": #todo add the login function
        print(red("Warning: You are playing as a guest! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
        functions.deal_or_no_deal()
    elif command.lower() == "tutorial":
        print(red("Warning: You are playing in tutorial mode! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
        functions.tutorial()
    elif command.lower() == "2":
        pass
    elif command.lower() == "3":
        pass
    elif command.lower() == "4":
        pass
    elif command.lower() == "highscore":
        pass
    elif command.lower() == "[settings]": 
        pass

if __name__ == "__main__":
    print("You know how to play this. Please add instructions later")
    #deal_or_no_deal() #TODO break this down into smaller functions
    while True:
        command = input("Type the correct command. Type HELP for help: ")
        if command.lower() == "exit":
            break
        cli(command)
