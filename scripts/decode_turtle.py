import turtle
import re

t = turtle.Turtle()

def find_number(line):
    return int(re.findall('[0-9]+', line)[0])

with open("turtle.txt", "r") as f:
    for line in f:
        if line.find("Tourne") > -1 and line.find("gauche") > -1:
            t.left(find_number(line))
        elif line.find("Tourne") > -1 and line.find("droite") > -1:
            t.right(find_number(line))
        elif line.find("Avance") > -1:
            t.forward(find_number(line))
        elif line.find("Recule") > -1:
            t.backward(find_number(line))
        else:
            t.clear()
