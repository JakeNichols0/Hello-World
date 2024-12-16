from time import sleep as wait
import random

def helloWorld(s):
    if(s == "p""r""i""n""t"):
        w = "H""e""l""l""o"" ""W""or""l""d""!"
    else:
        w = s
    j = ""
    for i in w:
        char = 0
        while (char != ord(i)):
            char = random.randint(32, 122)
            wait(char/10000)
        print(chr(char), end="")

helloWorld("print")


















