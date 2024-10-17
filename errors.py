#!/usr/bin/env python3
import os
import sys

#EAFP - easy to ask Foring than permission
#Exemplos
try:
    names = open("names.txt").readlines()
    2/2
    print(names.append)
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't have banana")
    sys.exit(1)


try:
    print(names[3])
except:
    print("[Error Missing nae in the list] ")
    sys.exit(1)