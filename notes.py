#!usr/bin.env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text:
Anotação sobre carreira de tecnologia

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"

import sys
import os

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys. argv[1:]

if not arguments:
    print("Invalid usage")
    print(f"voce não especificou os subcomandos que são{cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments == "read":
    #leitura de notas
    for line in open(filepath):
        titulo, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {titulo}")
            print(f"text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    titulo = arguments[1]#TODO Tratar exception
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
#\t - tsv
with open(filepath, "a") as file:
    file.write("\t".join(text) + "\n")





