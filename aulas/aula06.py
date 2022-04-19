# strings - p1

curso = "Curso de Python"

## selecionar índice ou intervalo da string
print(curso[3:9])

print("Tamanho: ", len(curso))

# método strip remove espaços no começo e no final

# método lower converte para minúsculo
print(curso.lower())

# replace faz a substituição
print(curso.replace("Python", "C#"))

# Split faz uma subdivisão na string
a = curso.split(" ")

print(a)
