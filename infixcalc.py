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
import sys
from datetime import datetime
arguments = sys.argv[1:]

if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
    print(operation)
elif len(arguments) != 3:
    print("Numeros invalidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)

operations, *nuns = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operations not in valid_operations:
    print("Operação invalida")
#    print(valid_operations)
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

