import pyfiglet

#finds charcters pyfiglet can print
def pyf(x, a):
    l = []
    for i in range(a, x+a):
        p = pyfiglet.figlet_format(chr(i))
        if(p.strip() and not chr(i).lower() in l):
            l.append(chr(i).lower())
    return l

for j in range(0, 10):
    print(pyf(1000, 1000*j+10000))

#Extra charaters: 'ಠ',
#print(pyfiglet.figlet_format("ಠ_ಠ"))