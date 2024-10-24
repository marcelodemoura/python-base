import os
import sys 
import smtplib
from email.mime.text import MIMEText 

arguments =sys.argv[1:]
if not arguments:
    print("Informar o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host = SERVER) as server:
    for line in open(filepath):
          name, email = line.split(",")
    text = (
        open(templatepath).read()
            % {
                "nome": name,
                "produto": "caneta",
                "texto": "Escreve muito bem",
                "link": "https://cantaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
                
        }
    )

    from_ = "marcelo.cavalcanti@mv.com.br"
    to_ =  ", ".join([email])
    
    message = MIMEText(text)
    message["Subject"] = "Compre mais"
    message["From"] = from_
    message["To"] = to_

    server.sendmail(from_, to_, message.as_string())
  

