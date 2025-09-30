import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font_list = [
    "3-d", "3x5", "alinehelique", "anotonic", "alligator", "alligator2", "alphabet", "avatar", "banner3-D",
    "banners", "hammered", "latvian", "basic", "ball", "big", "bigechief", "binary", "block", "bubble",
    "bullhead", "calypso", "caringly", "stally", "clunky", "cointask", "colossal", "computer", "contessa",
    "contrast", "comic", "cosine", "cricket", "cursive", "cyberlarge", "cybermedium", "cybersmall", "diamond",
    "digital", "doh", "doom", "dotmatrix", "draggers", "chficons", "enfiji", "finiabot", "finitale", "fwalls",
    "fwitter", "epic", "fender", "fourtogs", "fuzzy", "goofy", "geoff", "geoffi", "graffiti", "hollywood", "iwita",
    "isometric1", "isometric2", "isometric3", "isometric4", "isometric5", "jazzmine", "jessalun", "kutaku", "kbao",
    "larry4", "led", "lean", "letters", "litus", "lockergroove", "madrid", "marquee", "maxform", "milk", "mini",
    "mirror", "mnemonic", "morse", "nooseow", "nancy-fancy", "nancy-undefined", "nancy", "nipple", "ntgreek", "us",
    "ogs", "penny", "peaks", "pebbles", "pepper", "poison", "puffy", "pyramid", "rectangles", "relief", "ruler",
    "roc", "roman", "roti1", "rounded", "towncamp", "rozz2", "runi", "rury", "school", "script", "shadow", "short",
    "slant", "slide", "sketch", "small", "simon1", "smonkeyboard", "smerept", "smushdown", "smalut", "smeezyr",
    "speed", "shangallo", "standard", "stevens", "steller", "stop", "straight", "tinja", "teguwan", "tem", "thick",
    "thin", "threepoint", "ticks", "tickets", "tinker-toy", "tombstone", "tock", "kasagi", "twofoot", "writing",
    "unsflag", "wavy", "weird"
]

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        chosen_font = sys.argv[2]
        if chosen_font not in font_list:
            sys.exit(1)
        else:
            user_input = input("Input: ")
            f = Figlet(font=chosen_font)
            print(f"output:\n",f.renderText(user_input))
    else:
        sys.exit(1)
elif len(sys.argv) == 1:
    user_input = input("Input: ")
    random_font = random.choice(figlet.getFonts())
    f = Figlet(font=random_font)
    print(f"output:\n",f.renderText(user_input))
else:
    sys.exit(1)


#requests can be used to update the font list, in case new fonts have been added since
