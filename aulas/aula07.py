# strings - p2

curso = "Curso de Python"

# in verifica se a string informada consta dentro da variável
res = "Python" in curso

# adicionar not inverte a verificação
res_not = "python" not in curso


text = "Curso de Python"
palavra = "python"

# upper converte para maiusculo
res_new = palavra.upper() in text.upper()


curso2 = "Curso de Python"
canal = "CFB Cursos"

res_concat = curso2 + " " + canal

cidade = "Cajamar"
dia = 12
mes = "Abril"
ano = 2022

# string format: f"string {variavel} string"
res_data = f"{cidade}, {dia} de {mes} de {ano}"

# Caracteres de escape:
# \' \" \n \r \t \d

print(res_data)