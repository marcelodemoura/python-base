#!usr/bin/env python3

"""Hellow word multi linguas.
Dependendo da ligua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Ter a variavel Lang devidamente configurada ex: 

    esport LANG=pt_BR
"""

__version__ = "0.1.2"
__author__ = "Marcelo de Moura"

import os
import sys

arguments = {
    "lang":None,
    "count":3,
}

for arg in sys.argv[1:]:
   #TODO:Tratar ValueError
   key, value = arg.split("=")
   key = key.lstrip("-").strip()
   value = value.strip()
   if key not in arguments:
       print(f"Invalid option '{key}'")
       sys.exit()
   arguments[key] = value

#current_language = os.getenv("LANG","en_US")
#argsuments = {}
#for arg in sys.argv[1:]:
#    print(f"{sys.argv=}")

#current_language = "it_IT"

#current_language = current_language[:5]

current_language = arguments["lang"]  
if current_language is None:
    current_language = os.getenv("LANG","en_US")
    #TODO: repeticao
    if current_language is None:
        current_language = input("Qual linguagem utilizada:")

msg = {
    "en_US": "Hello word!",
    "pt_BR": "Ola Mundo",
    "it_IT": "Ciao Mondo",
    "es_ES": "Hola Mundo",
    "fr_FR": "Bonjour, Monde",
}

#print(msg[current_language] * arguments ["count"])
print(msg[current_language])