#!/usr/bin/env pytho3

import logging

log = logging.Logger("logs", logging.DEBUG)

#TODO transformar em função(loguru)

#level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#format o que o log mostrara
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s')

ch.setFormatter(fmt)
log.addHandler(ch)

"""
log.debug("msg dev")
log.info("msg usuarios")
log.warning("msg aviso que não causa erros")
log.error("msg erro que afeta apenas um usr")
log.critical("msg erro que afeta todo sistema")
"""

try:
    1/0
except ZeroDivisionError as e:
    log.error(f"[ERRO] Deu erro {str(e)}")