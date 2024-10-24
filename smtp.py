#!/usr/bin/env python3

import smtplib

SERVER = "localhost"
HOST = 8025
#lPORT = 8080
"""envio de e-mail"""

FROM = "marcelo.cavalcanti@mv.com.br"
TO = ["marcelodemoura14@gmail.com"]
SUBJECT = "E-mail via python"
TEXT = """/
E-mail enviado via python
<b>Óla mundo</b>
"""

#SMTP
mensagem = f"""/
From: {FROM} 
TO: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""
#TODO corrigir erro de porta e server aula 32
with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, mensagem.encode("utf-8"))