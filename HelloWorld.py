from time import sleep as wait
import random
import math
import pyfiglet
import colorama
import sympy
import sympy.plotting as pl

#To do list:
#-"Fix" equality
#-Randomize ascii art type
#-Add special characters to look like it's corrupted (Done partially, but I still need to figure out how to support more letters)

class Number:
    def __init__(self, groß=0):
        self.groß = groß

    def __str__(self):
        return chr(self.groß)
    
    def __eq__(self, value):
        if(self.groß == value.groß):
            ran = random.randint(0, 9)
            if(ran == 5) : #10% chance that it returns false even if they match
                return False
            else :
                return True
        else:
            return False
    
    def __add__(self, value):
        if(self.groß == value.groß):
            return self.groß * 2
        elif(self.groß == 0):
            return value.groß
        elif(value.groß == 0):
            return self.groß
        else:
            a = math.sqrt(self.groß) #Constants
            b = math.sqrt(value.groß)
            x = sympy.symbols('x') #Varibles
            anti0 = sympy.integrate(sympy.ln(a * x), x)
            anti1 = sympy.integrate(sympy.ln(b * x), x)
            d = sympy.diff(anti0 + anti1)
            terms = []
            for i in d.args:
                if(x in i.free_symbols):
                    terms.append(i)
            output = 0.0
            for j in terms:
                output += sympy.N(sympy.E**(j), subs = {x: 1})**2
            return int(str(output).split(".")[0])

    def out(self):
        return f"{self} ( {self.groß} )"

def test(x): #Tests addition for every number between 0 and x. x^2 tests
    err = 0
    for i in range(0,x):
        a = Number(i)
        for j in range(0,x):
            b = Number(j)
            weird = a + b
            normal = a.groß + b.groß
            if(weird != normal):
                print(f"{i} + {j}: Normal = {normal}, Weird = {weird}")
                err += 1
        print(f">>> {(i+1)*x} tests complete")
    print(f"Complete. {err} errors")

def color(s):
    ρ = Number(random.randint(0,3))
    if(ρ == Number(0)):
        print(colorama.Style.DIM, end="")
    elif(ρ == Number(1)):
        print(colorama.Style.NORMAL, end="")
    elif(ρ == Number(2)):
        print(colorama.Style.BRIGHT, end="")
    r = Number(random.randint(0,5))
    if(r == Number(0)):
        return colorama.Fore.RED + s
    elif(r == Number(1)):
        return colorama.Fore.YELLOW + s
    elif(r == Number(2)):
        return colorama.Fore.GREEN + s
    elif(r == Number(3)):
        return colorama.Fore.CYAN + s
    elif(r == Number(4)):
        return colorama.Fore.BLUE + s
    elif(r == Number(5)):
        return colorama.Fore.MAGENTA + s

def corrupt(l):
    options = {
        'a': ['a','ä', 'ā', 'ă', 'ą',], #'à','á','â','ã','å','æ'
        'b': ['b'],
        'c': ['c', 'ć', 'ĉ', 'ċ', 'č'], #'ç'
        'd': ['d', 'ď', 'đ'], #'ð'
        'e': ['e', 'ē', 'ĕ', 'ė', 'ę', 'ě'], #'è','é','ê','ë'
        'f': ['f'], #'ƒ'
        'g': ['g', 'ĝ', 'ğ', 'ġ', 'ģ'],
        'h': ['h', 'ĥ', 'ħ'],
        'i': ['i', 'ĩ', 'ī', 'ĭ', 'į', 'i̇', 'ı'], #'ì','í','î','ï'
        'j': ['j', 'ĵ'],
        'k': ['k', 'ķ', 'ĸ'],
        'l': ['l', 'ĺ', 'ļ', 'ľ', 'ŀ', 'ł'],
        'm': ['m'],
        'n': ['n','ń', 'ņ', 'ň', 'ŉ', 'ŋ'], #'ñ'
        'o': ['o','ö','œ', 'ō', 'ŏ', 'ő'], #'ò','ó','ô','õ','ø'
        'p': ['p'],
        'q': ['q'],
        'r': ['r', 'ŕ', 'ŗ', 'ř'],
        's': ['s','š','ß', 'ś', 'ŝ', 'ş', 'ſ'],
        't': ['t', 'ţ', 'ť', 'ŧ'], #'þ'
        'u': ['u','ü', 'ũ', 'ū', 'ŭ', 'ů', 'ű', 'ų'], #'ù','ú','û'
        'v': ['v'],
        'w': ['w', 'ŵ'],
        'x': ['x'],
        'y': ['y', 'ŷ', 'ÿ'], #'ý','ÿ'
        'z': ['z','ž', 'ź', 'ż']
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
    j = Number()
    scheiße = "" #0223
    würstchen = "" #0252
    versucht = Number()
    for i in w:
        char = Number()
        while (not (char == Number(ord(i)))):
            char.groß = random.randint(32, 122)
            j.groß += char.groß
            versucht.groß += 1
            wait(char.groß/10000)
        clear(würstchen)
        scheiße += corrupt(chr(char.groß))
        würstchen = pyfiglet.figlet_format(scheiße)
        print(color(würstchen))
        j.groß /= char.groß
    p = Number(math.floor(j.groß))
    print(colorama.Style.RESET_ALL)
    print("Run time: ", p.out()) #Isn't the actual runtime, just some number that means nothing
    print("Attempts: ", versucht.out())

helloWorld("print")












