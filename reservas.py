#!/usr/bin/env python3

'quartos.txt'
"""
# codigo, nome, preco
1 - Suite Master - R$ 500.00
2 - Qrato familia - R$ 200.00
3 - Quarto Single - R$ 100.00
4 - Quarto Duplo - R$ 50.00
"""
'reserva.txt'
#cliente, quarto, dias
"""Jose, 3, 12"""

import sys
import logging

RESERVA_FILE = "reserva.txt"
QUARTOS_FILE = "quartos.txt"

ocupados = {} # guarda
try:
    for line in open(RESERVA_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias":int(dias)
    }
except FileNotFoundError:
    logging.error("arquivo %s não existe", RESERVA_FILE)
    sys.exit(1)

quartos = {} # guarda
try:
    for line in open(QUARTOS_FILE):
       num_quarto, nome_quarto, preco = line.strip().split(",")
       quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preço": float(preco),
            "disponivel": False if int(num_quarto) in ocupados else True
    }
except FileNotFoundError:

    logging.error("arquivo %s não existe", QUARTOS_FILE)     
    sys.exit(1)

#PRINCIPAL
print("Reservas.com")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(0)

nome_cliente = input("Qual seu nome: ").strip()
print()
print("Lista de quartos")
print()
head = ["numero", "nome do quarto", "preço", "disponivel"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")

for num_quartos, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = dados_quarto["disponivel"]
    print(f"{num_quarto:<6} - {nome_quarto:<14} "
          f" R${preco:<9} - {disponivel:<10}")

print("-" * 52)
try:
    num_quarto = int(input("Qual quarto desejado: ").strip())
    if not quartos[int(num_quarto)]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupadpo, escolha outro.")
        sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)

try:
    dias = int(input("Quantos dias: ").strip())
except ValueError:
    print(f"Numero invalido digite apena numeros")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(
    f"Óla {nome_cliente}, você escolheu o quarto {nome_quarto}"   
    f"o valor total estimado será R$ {total:.2f}"
)

if input("Confirma? (digite y)").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVA_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")