from deal_no_deal_module import functions
from simple_colors import * #! pip install simple_colors
import time, os, keyboard #! pip install keyboard

#* Used for the highscores
def add_float_in_descending_order(numbers, new_number):
    #* Convert the strings to floats, and add the new float
    numbers = [float(n) for n in numbers] + [new_number]
    #* Sort the list in descending order
    numbers = sorted(numbers, reverse=True)
    #* Truncate the list to 10 elements if necessary
    if len(numbers) > 10:
        numbers = numbers[:10]
    #* Convert the floats back to strings and return the result
    return [str(n)+"\n" for n in numbers]

def cli():
    #* This is the command line interface
    #* It works by checking if a key is pressed, and if it is, it runs the corresponding function
    while True:
        if keyboard.is_pressed("a"):
            print("[A]: Displays this message\n[E]: To quit the app\n[L]ogin/Signup: Allows user login\n[M]ultiplayer tutorial: " \
                  "Gives you a tutorial for multiplayer mode. " + red("You need 2 people for this!\n", "bold") + ""\
                  "[T]utorial: Runs the game in tutorial mode\n[G]uest: To play as guest\n[2] player: Runs game in 2 player mode" \
                  "[3] player: Runs game in 3 player mode\n[4] player: Runs game in 3 player mode\n" \
                  "[H]ighscore: Shows the list of high scores\n[S]ettings: Allows user to turn background music on/off")
            time.sleep(1)
            keyboard.press("backspace")
            break
        elif keyboard.is_pressed("l"):
            keyboard.press("backspace")
            time.sleep(0.5)
            username = functions.login_or_signup()
            print(green(str("Welcome, " + username + "! Nice to see you back!"), "bold"))
            score = functions.deal_or_no_deal()
            num1 = 0
            with open("high.scores", "r") as f:
                scores = f.readlines()
            with open("high.scores", "w") as f:
                scores = add_float_in_descending_order(scores, score)
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
        elif keyboard.is_pressed("m"):
            print(red("Warning: You are playing in multiplayer tutorial mode! Your scores won't be considered for the highscore! CTRL + C to quit!", "bold"))
            keyboard.press("backspace")
            functions.mtutorial()
            break
        elif keyboard.is_pressed("2"):
            print(red("Warning: You are playing in multiplayer mode! Your scores won't be considered for the highscore! CTRL + C to quit!", "bold"))
            keyboard.press("backspace")
            functions.multiplayer(2)
            break
        elif keyboard.is_pressed("3"):
            print(red("Warning: You are playing in multiplayer mode! Your scores won't be considered for the highscore! CTRL + C to quit!", "bold"))
            keyboard.press("backspace")
            functions.multiplayer(3)
            break
        elif keyboard.is_pressed("4"):
            keyboard.press("backspace")
            print(red("Warning: You are playing in multiplayer mode! Your scores won't be considered for the highscore! CTRL + C to quit!", "bold"))
            functions.multiplayer(4)
            break
        elif keyboard.is_pressed("h"):
            keyboard.press("backspace")
            with open("high.scores", "r") as f:
                scores = f.readlines()
            highscores = ""
            for score in scores:
                highscores += magenta(score)
            print(highscores)
            time.sleep(0.5)
            break
        elif keyboard.is_pressed("s"):
            time.sleep(0.5)
            keyboard.press("backspace")
            functions.change_setting()
            break
        elif keyboard.is_pressed("e"):
            keyboard.press("backspace")
            return "break"


def main():
    print(green("Press the required key. Press A for assistance: "))
    if cli() == "break":
        return "break"

if __name__ == "__main__":
    output = ""
    while True:
        if functions.check_setting() == "no_music": #* This means no music
            functions.stop_background_music()
        elif functions.check_setting() == "music":
            functions.play_background_music()
        output = main()