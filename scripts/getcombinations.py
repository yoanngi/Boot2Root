#!/bin/sh

import itertools

path = "/home/eliott/BOMB/titi"

def isUniqueChars(st):
   if len(st) > 256:
      return False
   # Initialization
   char_set = [False] * 128
   # in char_set
   for i in range(0, len(st)):
      # ASCII value
      val = ord(st[i])
      if char_set[val]:
         return False
      char_set[val] = True
   return True

opened = open("combs", "r+")
for combination in itertools.product(range(10), repeat=6):
	x = ''.join(map(str, combination))
	if isUniqueChars(x):
		if (x[0] == "4"):
			opened.write(" ".join(str(x)) + "\n")
