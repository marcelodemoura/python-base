#!/usr/bin/env python3


#1- Faça um execricio que imprima os numeros pares de 1 a 200

"""for numbers in range(1,201):
    par = numbers % 2 == 0
    if par:
        print(numbers)
"""
#2 - Faça um script que receba do usuario a temperatura atual e o indice de
# humidadedo ar sabendo que caso sera exibido alerta dependendo da temperatura

"""
temp > 45 ALERTA calor extremo
temp 3 * >= A umidade: ALERTA!!! perigo de calor umido
temp entre 10 and 30: normal
temp entre 0 and 10: frio
temp <0: frio extremo
"""
import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura":None,
    "umidade": None
}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} invalida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("calor extremo")
elif temp * 3 >= umidade:
    print("ALERTA de Umidade")
elif temp >= 10 and temp<= 30:
    print("NORMAL")
elif temp >= 0 <= 10:
    print("FRIO")
elif temp < 0 :
    print("ALERTA frio extremo")



"""
#Repete vogal
words = [] 
while True:
    word = input("Digite uma palavra ou (enter para sair):").strip()
    if not word:
        break
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãêóíáà":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

for word in words:
    print(*word, sep = "")
"""



'quartos.txt'
#cliente, quartos, dias
"""
# codigo,nome,preco
1 - Suite Master - R$ 500.00
2 - Qrato familia - R$ 200.00
3 - Quarto Single - R$ 100.00
4 - Quarto Duplo - R$ 50.00
"""
'reservas.txt'
#cliente, quartos, dias
'Jose, 3, 12'
"""

import sys
import logging

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe") 
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),
            "disponivel": True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe") 
    sys.exit(1)

print("reservas.com")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("hotel lotado")
    sys.exit(1)

nome = input("Nome do cliente: ").strip()
print("Listas de quartos:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = dados['disponivel'] = True
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")

print("-" * 40)

try:
    num_quarto = int(input("Numero do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} esta ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Numero o quarto invalido")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe")

try:
    dias = int(input("Quantos dias?:").strip())
except ValueError:
    logging.error("Numero invalido, digite apenas numeros.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar R${total:.2f}")
"""