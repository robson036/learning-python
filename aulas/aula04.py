# Tipos de dados

# int
inteiro = 1

print('Valor: ', inteiro)
print('Tipo: ', type(inteiro)) # int

texto = 'Robson'

print('Valor: ', texto)
print('Tipo: ', type(texto)) # str

flutuante = 15.6

print('Valor: ', flutuante)
print('Tipo: ', type(flutuante)) # float

booleano = False

print('Valor: ', booleano)
print('Tipo: ', type(booleano)) # boolean

complexo1 = 5; complexo2=2; complex_res =  complex(complexo1, complexo2)

print('Valor: ', complex_res)
print('Tipo: ', type(complex_res)) # complex

######################

lista = ['Carro', 'Avião', 'Navio']

print('Valor: ', lista)
print('Valor: ', lista[1])
print('Tipo: ', type(lista)) # list

tupla = ('Carro', 'Avião', 'Navio')

print('Valor: ', tupla)
print('Valor: ', tupla[1])
print('Tipo: ', type(tupla)) # tuple

# Obs: Ao contrário do array, a tupla é imutável

dicionario = {
    'nome': 'Robson',
    'curso': 'Python'
}

print('Valor: ', dicionario)
print('Tipo: ', type(dicionario)) # dict

sett = {5,8,9,55,42,5,447,5,4,4,}

print('Valor: ', sett)
print('Tipo: ', type(sett)) # set