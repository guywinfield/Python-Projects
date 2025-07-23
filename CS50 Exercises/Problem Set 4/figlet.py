import sys
from pyfiglet import Figlet
import random

figlet = Figlet()


def main():
    figlettize("Input: ")


def figlettize(prompt):
    font_list = figlet.getFonts()

    if len(sys.argv[1:]) == 2:
        if sys.argv[-1] not in font_list:
            sys.exit("Invalid usage")
        elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
            raw_text = input(prompt)
            figlet.setFont(font=sys.argv[-1])
            print(figlet.renderText(raw_text))
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv[1:]) == 0:
        raw_text = input(prompt)
        random_font = random.choices(figlet.getFonts())
        figlet.setFont(font=random_font[0])
        print(figlet.renderText(raw_text))

    else:
        sys.exit("Invalid usage")

main()

