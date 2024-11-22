import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts_list = figlet.getFonts()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    random_font = random.choice(fonts_list)
    figlet.setFont(font=random_font)
    print(figlet.renderText(user_input))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in fonts_list:
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(user_input))
        else:
             sys.exit("Font does not exist.")
else:
    sys.exit("Usage: figlet.py [-f font_name | --font font_name]")