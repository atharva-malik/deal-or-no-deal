"""ASCII Art Generator
import PIL.Image

# ascii characters used to build the output text.
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    # attempt to open image
    path = input("Enter valid path: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not valid.")
        raise SystemExit
    
    # convert to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print the art
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()
"""

"""AUDIO PLAYER
from playsound import playsound #! pip install playsound==1.2.2
import os

audio_file = os.path.dirname(__file__) + '\\KomuramBheemudo.mp3'
playsound(audio_file)
"""

"""COLOURS IN TERMINAL
from simple_colors import * #! pip install simple_colors

all_colours = ["black", "red", "green", "yellow", "blue", "magenta", "cyan"]

all_styles = [
    "bright",
    "bold",
    "dim",
    "italic",
    "underlined",
    "blink",
    "reverse"
]

for style in all_styles:
    print(style, ": ", red('red', style), "\n")
    print(style, ": ", green('green', style), "\n")
"""

"""MULTI THREADING
import _thread
import random
from playsound import playsound #! pip install playsound==1.2.2
import os

# Define a function for the thread
def background_music():
    audio_file = os.path.dirname(__file__) + '\\KomuramBheemudo.mp3'
    playsound(audio_file)


def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases) #TODO: Try to make this more exciting
    return offer


def deal_or_no_deal():
    briefcases= {}
    offer = 0
    for i in range(1, 27):
        briefcases[str(i)] = random.randint(1, 1000000)
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    briefcases_to_eliminate = 6
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for i in range(0, briefcases_to_eliminate):
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    print("Remaining briefcases:", briefcases, "List", remaining_briefcases, "\nOffer: $", offer)
    while briefcases_to_eliminate >= 1:
        offer = get_offer(briefcases)
        print("Remaining briefcases:", len(remaining_briefcases), remaining_briefcases, "Offer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [n]o deal? ")
        if choice.lower() == "d":
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
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
                briefcases_to_eliminate -= 1
        else:
            continue


# Create two threads as follows
try:
    _thread.start_new_thread( background_music, ())
    _thread.start_new_thread( deal_or_no_deal, ())
except:
    print ("Error: unable to start thread")

while 1:
    pass
"""