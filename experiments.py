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


