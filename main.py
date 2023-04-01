from deal_no_deal_module import functions
from simple_colors import * #! pip install simple_colors
import time, os, keyboard

def cli():
    while True:
        if keyboard.is_pressed("a"):
            print("""[A]: Displays this message
CTRL + C: To quit the app
[L]ogin: Allows user login
[T]utorial: Runs the game in tutorial mode
[G]uest: To play as guest
[2] player: Runs game in 2 player mode
[3] player: Runs game in 3 player mode
[4] player: Runs game in 3 player mode
[H]ighscore: Shows the list of high scores
[S]ettings: Allows user to change the settings""")
            time.sleep(1)
            break
        elif keyboard.is_pressed("l"): #todo add the login function
            pass
        elif keyboard.is_pressed("g"):
            print(red("Warning: You are playing as a guest! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
            functions.deal_or_no_deal()
            break
        elif keyboard.is_pressed("t"):
            print(red("Warning: You are playing in tutorial mode! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
            functions.tutorial()
            break
        elif keyboard.is_pressed("2"):
            pass
        elif keyboard.is_pressed("3"):
            pass
        elif keyboard.is_pressed("4"):
            pass
        elif keyboard.is_pressed("h"):
            pass
        elif keyboard.is_pressed("s"):
            time.sleep(0.5)
            functions.change_setting()
            break
    keyboard.press("backspace")

if __name__ == "__main__":
    while True:
        print("Press the required key. Press A for assistance: ")
        cli()
