#!/usr/bin/env python3

"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações: 

sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2

$ infixcalc.py mul 10 5

$ infixcalc.py 

operação: sum
n1: 5 
n2: 4

Os resultados salvos em ´infixcalc.log´

"""
__version__ = "0.1.0"
import os
import logging
import sys
from datetime import datetime


log = logging.Logger("logs", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = sys.argv[1:]
try:
    operations, *nuns = arguments
except Exception as e:
    print(str(e))
    print("Numeros invalidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)
valid_operations = ("sum", "sub", "mul", "div")
if operations not in valid_operations:
    print("Operação invalida")
    sys.exit(1)

validated_nums = []
for num in nuns: 
    if not num.replace(".","").isdigit():
        print(f"Numero invalido {num}")
        sys.exit
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums
#TODO usar dit de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} {user}- {operation},{n1},{n2} = {result} \n")

print(f"O resultsdo é {result}")

