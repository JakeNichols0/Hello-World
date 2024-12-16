from time import sleep as wait
import random
import math

def helloWorld(s):
    if(s == "p""r""i""n""t"):
        w = "H""e""l""l""o"" ""W""or""l""d""!"
    else:
        w = s
    j = 0
    for i in w:
        char = 0
        while (math.sqrt(char) != math.sqrt(ord(i))):
            char = random.randint(32, 122)
            j += char
            wait(char/10000)
        print(chr(char), end="")
        j /= char
    print("\n", char(math.floor(j)))

helloWorld("print")


















