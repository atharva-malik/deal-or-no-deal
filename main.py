from deal_no_deal_module import functions
from simple_colors import * #! pip install simple_colors
import time, os, keyboard

def cli():
    while True:
        if keyboard.is_pressed("a"):
            print("""[A]: Displays this message
CTRL + C: To quit the app
[L]ogin/Signup: Allows user login
[T]utorial: Runs the game in tutorial mode
[G]uest: To play as guest
[2] player: Runs game in 2 player mode
[3] player: Runs game in 3 player mode
[4] player: Runs game in 3 player mode
[H]ighscore: Shows the list of high scores
[S]ettings: Allows user to change the settings""")
            time.sleep(1)
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("l"):
            keyboard.press("backspace")
            time.sleep(0.5)
            username = functions.login_or_signup()
            print(green(str("Welcome, " + username + "! Nice to see you back!"), "bold"))
            score = functions.deal_or_no_deal() #todo Store this for pb!
            with open("high.scores", "r") as f:
                scores = f.readlines()
            with open("high.scores", "w") as f:
                scores.append(str(score))
                f.writelines(scores)
            break
        elif keyboard.is_pressed("g"):
            print(red("Warning: You are playing as a guest! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
            keyboard.press("backspace")
            functions.deal_or_no_deal()
            break
        elif keyboard.is_pressed("t"):
            print(red("Warning: You are playing in tutorial mode! Your score won't be considered for the highscore! CTRL + C to quit!", "bold"))
            keyboard.press("backspace")
            functions.tutorial()
            break
        elif keyboard.is_pressed("2"):
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("3"):
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("4"):
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("h"):
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("s"):
            time.sleep(0.5)
            keyboard.press("backspace")
            functions.change_setting()
            break

if __name__ == "__main__":
    while True:
        print("Press the required key. Press A for assistance: ")
        cli()
