# Estrutra de decisão IF/ELIF/ELSE

# Operadores lógicos
"""
> - Maior
< - Menor
== - Comparação

or
and
"""

a = 10
b = 5
operacao = "+"

# Bloco if
if operacao == "+":
    print("Soma: ", a + b)


# Bloco elif
if operacao == "+":
    print("Soma")
elif operacao == "-":
    print("Subtração")
elif operacao == "/":
    print("Divisão")
else:
    print("Multiplicação")


idade = 30

maior = True if idade > 18 else False

print(maior)

print("Fim do programa")

