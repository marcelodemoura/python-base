#!/usr/bin/env python3
import os
import sys

#EAFP - easy to ask Foring than permission
#Exemplos
try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)


try:
    print(names[3])
except:
    print("[Error Missing nae in the list] ")
    sys.exit(1)