#!/usr/bin/env python3
import os
import sys

#EAFP - easy to ask Foring than permission
try:
    names = open("names.txt").readlines()
except:
    print("[Error] File names.txt not found.")
    sys.exit(1)

try:
    print(names[5])
except:
    print("[Error ] missing name in the list")
    sys.exit(1)