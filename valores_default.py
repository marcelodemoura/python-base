import time

def imprimir_nome(nome, sobrenome="capivara"):
    #escopo local {nome, ... sobrenome: ..}
    print (f"Seu nome e: {nome} {sobrenome}")

imprimir_nome("Jose", "da Silva")
imprimir_nome("Maria", "Jose")
imprimir_nome("Ana")


def conecta(host, timeout = 10):
    print(f"conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(i)
        print("." * i)
    print("erro ao conectar com o servidor")

conecta("localhost")
