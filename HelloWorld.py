from time import sleep as wait
import random
import math
import pyfiglet
import colorama

#To do list:
#-"Fix" equality
#-Randomize ascii art type
#-Add special characters to look like it's corrupted (Done partially, but I still need to figure out how to support more letters)
def color(s):
    ρ = random.randint(0,3)
    if(ρ == 0):
        print(colorama.Style.DIM)
    elif(ρ == 1):
        print(colorama.Style.NORMAL)
    elif(ρ == 2):
        print(colorama.Style.BRIGHT)
    r = random.randint(0,5)
    if(r == 0):
        return colorama.Fore.RED + s
    elif(r == 1):
        return colorama.Fore.YELLOW + s
    elif(r == 2):
        return colorama.Fore.GREEN + s
    elif(r == 3):
        return colorama.Fore.CYAN + s
    elif(r == 4):
        return colorama.Fore.BLUE + s
    elif(r == 5):
        return colorama.Fore.MAGENTA + s

def corrupt(l):
    options = {
        "a": ["a","ä"], #"à","á","â","ã","å","æ"
        "b": ["b"],
        "c": ["c"], #"ç"
        "d": ["d"], #"ð"
        "e": ["e"], #"è","é","ê","ë"
        "f": ["f"], #"ƒ"
        "g": ["g"],
        "h": ["h"],
        "i": ["i"], #"ì","í","î","ï"
        "j": ["j"],
        "k": ["k"],
        "l": ["l"],
        "m": ["m"],
        "n": ["n"], #"ñ"
        "o": ["o","ö","œ"], #"ò","ó","ô","õ","ø"
        "p": ["p"],
        "q": ["q"],
        "r": ["r"],
        "s": ["s","š"],
        "t": ["t"], #"þ"
        "u": ["u","ü"], #"ù","ú","û"
        "v": ["v"],
        "w": ["w"],
        "x": ["x"],
        "y": ["y"], #"ý","ÿ"
        "z": ["z","ž"]
    }
    low = l.lower()
    if(low in options.keys()):
        r = options[low][random.randint(0,len(options[low])-1)]
    else:
        r = l
    if(not l.islower()):
        r = r.upper()
    return r

def clear(pre):
    for i in range(pre.count("\n") + 1):
        print("\033[1A""\x1b[2K", end="")

def helloWorld(s):
    if(s == "p""r""i""n""t"):
        w = "H""e""l""l""o"" ""W""or""l""d""!"
    else:
        w = s
    j = 0
    Scheiße = ""
    Würstchen = ""
    for i in w:
        char = 0
        while (math.sqrt(char) != math.sqrt(ord(i))):
            char = random.randint(32, 122)
            j += char
            wait(char/10000)
        clear(Würstchen)
        Scheiße += corrupt(chr(char))
        Würstchen = pyfiglet.figlet_format(Scheiße)
        print(color(Würstchen))
        j /= char
    print(colorama.Style.RESET_ALL)
    print("Run time = ", chr(math.floor(j)))

helloWorld("print")














