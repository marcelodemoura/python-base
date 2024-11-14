#escopo GLOBAL
nome = "Global"
numero = 1
flag = True

def funcao():
    #escopo global da função
    nome = "Local"

    def funcao_interna(): #inner function
    # função local
        nome = "Interna"
        print(nome)
        return nome
    #termina o escopo local da função interna
    print("Escopo local da funcao:", locals())
    funcao_interna()
    print(nome)

    return nome
print("Escopo Global do programa", globals())

print("-" * 30)
funcao()
print(nome)
#termina escopo global




