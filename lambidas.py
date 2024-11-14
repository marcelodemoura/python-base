def transforma_em_maiuscula(texto):
    return texto.upper()

def transforma_em_maiuscula(texto):
    return texto.lower()

def divide_por_2(numero):
    return numero // 2

def faz_algo(valor, funcao):
    print(f"Aplica{funcao} em {valor}")
    return funcao(valor)


names = ["z","b","o","d"]
print(sorted(names))


#dicionario calculadora

operacao = input("operacao [sum, sub, mul, div]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}
 
resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é {resultado}")