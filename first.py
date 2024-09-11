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

current_language = os.getenv("LANG","en_US")

#current_language = "it_IT"

msg = {
    "en_US": "Hello word!",
    "pt_BR": "Ola Mundo",
    "it_IT": "Ciao Mondo",
    "es_ES": "Hola Mundo",
    "fr_FR": "Bonjour, Monde",
}

print(msg[current_language])