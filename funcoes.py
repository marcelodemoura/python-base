"""Exemplo de fonções""" 

"""
f(x) = 5 * (x / 2)
"""

#solid single Responsability

"""def f(x):
    result = 5 * (x/2)
    return result

def double(x):
    return x * 2

valor = double(f(10))

print(f(valor))
print(valor == 50)


def print_in_upper(text):
    print(text.upper())

print_in_upper("jose")"""

def heron (a, b, c):
    perimetro = a + b + c
    s = perimetro / 2
    area = s * (s-a) * (s - b) * (s - c)
    return area ** 0.5 #raiz quad area

def heron2 (params):
    return heron(*params)

triangulos = [
    (3,4,5),
    (5,12,13),
    (8,15,17),
    (12,35,37),
    (3,4,5),
    (5,12,13),
    (8,15,17),
    (12,35,37)
]

#print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron(*t)
    print(f"A area do  triangulo é: {area}")

for t in triangulos:
    area = heron2(t)
    print(f"A area do  triangulo é: {area}")

"""anotacoes/
"""
#definição ou atribuição
#assinatura
#documentos
#valor de retorno

def nome_da_funcao(a, b ,c):
     """ explicação sobre qas ações da função"""

     resultado = a + b + c
     return resultado
print(nome_da_funcao(1, 2 ,3))



