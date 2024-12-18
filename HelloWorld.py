from time import sleep as wait
import random
import math
import pyfiglet

def clear(pre):
    for i in range(pre.count("\n")+1):
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
        Scheiße += chr(char)
        Würstchen = pyfiglet.figlet_format(Scheiße)
        print(Würstchen)
        j /= char
    print("\n", char(math.floor(j)))

helloWorld("print")


















