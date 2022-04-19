from os import system
system("clear")
# Funções
# É um bloco de código para ser executado em um momento específico

def printar():
    print("Curso de Python")


n1 = 10
n2 = 5

def somar():
    r = n1 + n2
    print(f"Soma de {n1} e {n2} igual a {r}")

def sub():
    r = n1 - n2
    print(f"Subtração de {n1} e {n2} igual a {r}")

def somar_com_argumentos(num1: float, num2: float):
    r = num1 + num2
    print(f"Subtração de {num1} e {num2} igual a {r}")


def somar_com_muitos_argumentos(*n):
    r = 0
    for i in n:
        r += i
    print(r)


def funcao_que_retorna_valor(num1: float, num2: float):
    r = num1 + num2
    return r

res = funcao_que_retorna_valor(2, 5.2)
print(res)