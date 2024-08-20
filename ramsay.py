from sys import argv
import sys
import getopt
import random

xlist = [
    "My gran could do better... AND SHE'S DEAD.", \
    "for what we are about to eat, may the lord make us truly not vomit.", \
    "this lamb is so undercooked, it's following mary to school!", \
    "this pizza is so disgusting, if you take it to italy you'll get arrested.", \
    "this steak is so burnt, luke thought it was his uncle owen.", \
    "you used so much oil, the U.S. wants to invade the plate.", \
    "your food is so bad even a canadian would insult you.", \
    "this fish is so raw he's still finding nemo.", \
    "this isn’t a pizza, this is a mistake. this is an italian tragedy.", \
    "there’s enough garlic in here to kill every vampire in rurope.", \
    "hey, panini head, are you even listening to me?", \
    "i grew up in a funny way.", \
    "this crab is so undercooked i can still hear it singing ‘under the sea!’", \
    "i dress for women and i undress for men."
]

x = random.choice(xlist)    

ralsaymode = False
helpmode = False
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hc:l:")
except: 
    print("unexpected error occured, exiting")
for opt, arg in opts:
    if opt in ['-c']:
        x = arg
    elif opt in ['-l']:
        x = arg
        ralsaymode = True
    elif opt in ['-h']: 
        helpmode = True
    else:
        print("unexpected flag... exiting")

if helpmode == True:
    print("HELP MODE")
    print("help mode (-h)")
    print("      gives you this screen")
    print("      example:")
    print("              ramsay -h")
    print("custom mode (-c)")
    print("      prints out a custom word after the launch option")
    print("      use double quotes for more than one word")
    print("      example:")
    print('              ramsay -c "helooooo hai hai hai"')   
    print("ralsay mode (-l)")
    print("      ralsay mode (works exactly like custom mode)")
    print("      example:")
    print("              ramsay -l uhm")
    print("")
    print("try the commands, adapt to the syntax, its pretty easy tbh")

elif ralsaymode == True:
    dashdash = "-" * len(x)
    print("           -^-         ")
    print("       _/\\/_  \\/\\_     ")
    print(f"      (____ ))____)     {dashdash}")
    print(f"       / -     - \\     ({x})")
    print(f"      / ( ^)-(^ ) \\   / {dashdash}")
    print("     / ____v-v____ \\ / ")
    print("       \\-  -__---/     ")       
    print("       /  / V     \\       ")
    print("      /__/\\   /    \\   ")
    print("     =      V       =  ")
    print("   _=_              _=_")
    print("     -=---______---=-  ")
    print("        _| | | |       ")
    print("       (___- -___)     ")
else:
    dashdash = "-" * len(x)
    print("                                ")
    print(" ⠁⡼⠋⠀⣆⠀⠀⣰⣿⣫⣾⢿⣿⣿⠍⢠⠠⠀⠀⢀⠰⢾⣺⣻⣿⣿⣿⣷⡀⠀ ")
    print(" ⣥⠀⠀⠀⠁⠀⠠⢻⢬⠁⣠⣾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠐⠱⠏⡉⠙⣿⣿⡇⠀ ")
    print(f" ⢳⠀⢰⡖⠀⠀⠈⠀⣺⢰⣿⢻⣾⣶⣿⣿⣶⣶⣤⣤⣴⣾⣿⣷⣼⡆⢸⣿⣧⠀  {dashdash}")
    print(f" ⠈⠀⠜⠈⣀⣔⣦⢨⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⣼⠛⢹⠀ ({x})")
    print(f" ⠀⠀⠀⠀⢋⡿⡿⣯⣭⡟⣟⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⠀/ {dashdash}")
    print(" ⡀⠐⠀⠀⠀⣿⣯⡿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣉⢽⣿⡆  /")
    print(" ⢳⠀⠄⠀⢀⣿⣿⣿⣿⣿⣿⣿⠙⠉⠉⠉⠛⣻⢛⣿⠛⠃⠀⠐⠛⠻⣿⡇ /")
    print(" ⣾⠄⠀⠀⢸⣿⣿⡿⠟⠛⠁⢀⠀⢀⡄⣀⣠⣾⣿⣿⡠⣴⣎⣀⣠⣠⣿⡇/")
    print(" ⣧⠀⣴⣄⣽⣿⣿⣿⣶⣶⣖⣶⣬⣾⣿⣾⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⡇⠀⠀ ")
    print(" ⣿⣶⣈⡯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣹⢧⣿⣿⣿⣄⠙⢿⣿⣿⣿⠇⠀⠀ ")
    print(" ⠹⣿⣿⣧⢌⢽⣻⢿⣯⣿⣿⣿⣿⠟⣠⡘⠿⠟⠛⠛⠟⠛⣧⡈⠻⣾⣿⠀⠀⠀ ")
    print(" ⠀⠈⠉⣷⡿⣽⠶⡾⢿⣿⣿⣿⢃⣤⣿⣷⣤⣤⣄⣄⣠⣼⡿⢷⢀⣿⡏⠀⠀⠀ ")
    print(" ⠀⠀⢀⣿⣷⠌⣈⣏⣝⠽⡿⣷⣾⣏⣀⣉⣉⣀⣀⣀⣠⣠⣄⡸⣾⣿⠃⠀⠀⠀ ")
    print(" ⠀⣰⡿⣿⣧⡐⠄⠱⣿⣺⣽⢟⣿⣿⢿⣿⣍⠉⢀⣀⣐⣼⣯⡗⠟⡏⠀⠀⠀⠀ ")
    print(" ⣰⣿⠀⣿⣿⣴⡀⠂⠘⢹⣭⡂⡚⠿⢿⣿⣿⣿⡿⢿⢿⡿⠿⢁⣴⣿⣷⣶⣦⣤ ")
    print("                                ")
