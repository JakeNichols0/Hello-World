import re
import io

spec = ["Ä","Ö","Ü","ä","ö","ü","ß"]

with open("standard.flf", "r") as file:
    for a in range(12): # Ingonres top
        file.readline()
    chars = file.read().split("@@\n")
    letters = {}
    for char in chars:
        char = char.replace("@", "")
        char = char.replace("$", " ")
        lines = char.split("\n")
        if(re.search("^\dx",lines[0])):
            place = ""
            exec(f"place = '\\U0000{lines[0][2:6]}'")
            letters[place] = lines[1:]
        elif (re.search("^\d",lines[0])):
            letters[chr(int(lines[0].split()[0]))] = lines[1:]
        elif (len(letters)>94 and len(letters)<102):
            letters[spec[len(letters)-95]] = lines
        else:
            letters[chr(len(letters)+32)] = lines

with io.open("font.txt", mode="w", encoding="utf-8") as font:
    font.write(str(letters))
