# Coleção List
# Array


carros = ["HRV", "Golf", "Argo", "Focus"]

print(carros)

# imprime pela indezação

print(carros[0]) # HRV
print(carros[1]) # Golf

# Imprime da direita pra esquerda

print(carros[-1]) # Focus

# troca elemento do índice 3
carros[3] = "Fusion"

# Adicionar elementos
carros.append("Fit")
carros.append("Polo")

print(carros)

# len mostra o tamanho da lista
print(len(carros))

# remover item da lista

carros.remove("Fusion")

print(carros)

# pop remove o último item da lista

carros.pop()

print(carros)

# del remove o item pelo indice

del carros[2]

print(carros)

# clear limpa todos os elementos da lista

carros.clear()
print(carros)