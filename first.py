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
import logging


log = logging.Logger("logs", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang":None,
    "count":3,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "you need to use '=', voce tem que passar %s, try --key=value: %s",
            arg, str(e)
        )
        sys.exit(1)
#for arg in sys.argv[1:]:
#    try:
#        key, value = arg.split("=")
#    except ValueError as e:
#        print("you need to use '='")
#        print(f"[ERROR] {str(e)}")
#        sys.exit(1)


    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
       print(f"Invalid option '{key}'")
       sys.exit()
    arguments[key] = value

current_language = arguments["lang"]  
if current_language is None:
    if "LANG" in os.environ:
         current_language = os.getenv("LANG")
    else: 
        current_language = input("Qual linguagem utilizada:")
  
        #current_language = "it_IT"
current_language = current_language[:5]

msg = {
    "en_US": "Hello word!",
    "pt_BR": "Ola Mundo",
    "it_IT": "Ciao Mondo",
    "es_ES": "Hola Mundo",
    "fr_FR": "Bonjour, Monde",
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
