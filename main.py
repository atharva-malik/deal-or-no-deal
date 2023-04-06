from deal_no_deal_module import functions
from simple_colors import * #! pip install simple_colors
import time, os, keyboard


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
    while True:
        if keyboard.is_pressed("a"):
            print("""[A]: Displays this message
[E]: To quit the app
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
        elif keyboard.is_pressed("2"): # todo add 2 player, 3 player, and 4 player mode
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
            with open("high.scores", "r") as f:
                scores = f.readlines()
            highscores = ""
            for score in scores:
                highscores += magenta(score)
            print(highscores)
            time.sleep(0.5)
            break
        elif keyboard.is_pressed("s"): # todo add actual sounds to make this work!!!
            time.sleep(0.5)
            keyboard.press("backspace")
            functions.change_setting()
            break
        elif keyboard.is_pressed("e"):
            keyboard.press("backspace")
            return "break"


#def background_music():



def main():
    while True:
        print(green("Press the required key. Press A for assistance: "))
        if cli() == "break":
            break

if __name__ == "__main__":
    if functions.check_setting() == "no_music": #This means no music
        main()
    elif functions.check_setting() == "music":
        functions.play_background_music()
        main()
