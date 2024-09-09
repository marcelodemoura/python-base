#!usr/bin/env python3

"""Hellow word multi linguas.
Dependendo da ligua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Ter a variavel Lang devidamente configurada ex: 

    esport LANG=pt_BR
"""

__version__ = "0.0.1"
__author__ = "Marcelo de Moura"
import os

current_language = os.getenv("LANG")

#current_language = "it_IT"

msg = "Hello word!"

if  current_language == "pt_BR":
    msg = "Ola, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)