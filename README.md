# Deal or no Deal

This game is clone of the popular show, Deal or no Deal. It comes with a wide variety of features like, user login and sign up, multiplayer, background music, CLI interface, settings, multiple tutorials, Web app interface, etcetera. It is fully functional and extremely easy to use!

## Features

- Easy to use
- Thoroughly commented and easily editable python code 
- Comes with basic CLI interface
- Comes with basic Web app interface
- Comes with a basic user login and sign up system
- Encrypted password storage for extra security
- Background music to help you concentrate in-game

## Technologies Used (CLI)

This console application uses 2 main technologies on the front end, [Python 3.10] and the [simple-colors] module, but uses lots of different technologies in the background like the keyboard module (to take user input in a more intuitive manner) and [PyGame] (to help with the background music)


## Technologies Used (Web app)

This web application uses 2 main technologies on the front end, [Python 3.10] and the [flask] module, but uses lots of different technologies in the background like JavaScript (to make the web app more interactive and functional, even offline) and [PyGame] (to help with the background music)


## Installation

Install the repository and the following packages and you are good to go!
```sh
pip install -r .\requirements.txt
```

## Execution for CLI version
To run the script, navigate to the directory of installation. From there, go to CODE FOR CLI, open it in terminal and type:
```sh
py -3 main.py
```
Then press "L" on your keyboard to create your account or login to the default account.

The default username and password are:
* Username: admin
* Password: admin

## Execution for Web app version
To run the script, navigate to the directory of installation, open it in terminal and type:
```sh
py -3 app.py
```
The default username and password are:
* Username: admin
* Password: admin

## <span style="color:#FF0000;">WARNING</span> 

The keyboard module used in the CLI is very dangerous and therefore I recommend that you do not allow this script to run in the background as it will record all keystrokes while the script is running. It will also press keys like "backspace" to try and counteract the effects of keys being stored in the RAM. This can be dangerous if you are not in the terminal window as this can delete your work!

## Development


Want to contribute? Great! Pull requests and issues are welcome! [Here] is an excellent guide on how to create pull requests and forks to request changes. I suggest using the addon "Better Comments" on Visual Studio Code as it makes the comments more readable. If you can not use the addon, I have used the following tags to make the comments more readable:

- #todo: This is a todo
- #*: This explains the code
- #!: This is a warning

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

   [PyGame]: <https://www.pygame.org/>
   [Python 3.10]: <https://www.python.org/downloads/release/python-3109/>
   [simple-colors]: <https://pypi.org/project/simple-colors/>
   [Here]: <https://www.dataschool.io/how-to-contribute-on-github/>
   [flask]: <https://pypi.org/project/Flask/>


### Credits
Music by Eric Matyas

www.soundimage.org

Image from Linkedin
