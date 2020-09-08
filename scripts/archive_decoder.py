import os, re, operator

import time

content = {}
directory = os.listdir('./')
for element in directory:
    if element != "script.py":
        with open(element, "r") as f:
            myfile = f.read()
            if re.findall('file', myfile) > -1:
                number = re.findall('//file([0-9]+)', myfile)
                print(number)
                if len(number) > 0:
                    content[int(number[0])] = str(myfile)

with open("programme_final.c", "w") as f:
    for element in sorted(content.keys()):
        f.write(content[element])
                






