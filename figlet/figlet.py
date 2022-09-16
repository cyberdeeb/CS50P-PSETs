from pyfiglet import Figlet
import random
import sys

def font():

    # Verify number of command line arguments
    if len(sys.argv) == 1:
        randomFont = True
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        randomFont = False
    else:
         sys.exit('Invalid usage')

    # Get a list of available fonts
    figlet = Figlet()
    figlet.getFonts()

    # Check if image will need randomized font and then set the font
    if randomFont == True:
        font = random.choice(figlet.getFonts())
    else:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit('Invalid usage')


    txt = input('Input: ')

    # Output text in set font
    print(figlet.renderText(txt))

font()