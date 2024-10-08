#!usr/bin/env python3
"""Relatorio de crianças por atividade

Imprime a lista de crianças destribuidas por sala
que frequenta cada atividade.
"""
__version__ = "0.1.1"

sala1 = ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria","Isolda"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca =  ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Ingles",aula_ingles),
              ("Musica", aula_musica),
              ("Dança",aula_danca),
              ]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"sala1", atividade_sala1)
    print(f"sala2", atividade_sala2)





