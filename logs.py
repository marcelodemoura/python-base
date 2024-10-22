#!/usr/bin/env pytho3
import os
import logging
from logging import handlers

#TODO transformar em função(loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs", logging.DEBUG)
#ch = logging.StreamHandler() # envia para console/terminal/stender
#ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "mlog.log",
    maxBytes=800, #o mais comum e usar 10**6
    backupCount=10,
    )



fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s')
#ch.setFormatter(fmt)
#log.addHandler(ch)
fh.setFormatter(fmt)
log.addHandler(fh)



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