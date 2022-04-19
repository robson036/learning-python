# Variáveis globais
num1=num2=res=0


def cn():
    # Para transformar uma variavel em global, colocar a palavra global antes do nome
    global canal
    canal = 'CFB Cursos'


cn()

print(canal)