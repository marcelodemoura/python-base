#!/usr/bin/env python3

#numbers = [1,2,3,4,5,6]
"""numbers = range(1,700)

for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue
    print(f"codigo com{number}")"""
"""
dados = {}
for line in open ("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()  
    print(dados)"""

"""original = [1,2,3]

#for loop
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

#List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)"""

#dict comprension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open ("post.txt")
    if":" in line
}

dados = {}
for line in open ("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)
