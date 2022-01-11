

idades = [15, 87, 65, 32, 56, 32, 49, 37]
# Método range + o tamanho da lista. vai de 0 ate o tamanho da lista.
for i in range(len(idades)):
    print(f'{i} - {idades[i]}')

print()
# enumerate com lista:
enumerates = list(enumerate(idades))
print(enumerates)
print()

# Enumerate com for:
for posicao in enumerate(idades):
    print(posicao)
print()

# unpacking da tupla: desempacotamento da tupla:
for indice, valor in enumerate(idades):
    print(f'Posição {indice} - valor: {valor}')
print()

# Desempacotamento das tuplas:
usuarios = [('Diego', 33, 1988),
            ('Thycianne', 33, 1988),
            ('Levi', 2, 2020)]

# Imprimindo as tuplas:
for usuario in usuarios:
    print(usuario)

# Desempacotando a tupla e imprimindo somente nome e idade
for nome, idade, ano in usuarios:
    print(f'Nome: {nome},  idade: {idade} anos')

print()
# Desempacotando a tupla e imprimindo somente nome, porem Desempacotando todos os valores da tupla.
for nome, idade, ano in usuarios:
    print(f'Nome: {nome}')

print()
# Desempacotando somente o nome, sem precisar desempacotar os demais valores:
for nome, _, _ in usuarios:
    print(f'Nome: {nome}')
print()

# Ordenação Crescente:
print(sorted(idades))
# Ordenação decrescente:
print(sorted(idades, reverse=True))
print(idades)
# Deixando a lista pra sempre ordenada:O idades.sort(), a lista original seria alterada, pois esse comando, além de ordenar, atribui o valor à lista
# original.
idades.sort()
print(idades)
print()

# Ordenando string's:
nomes = ['Diego', 'Levi', 'Thyci', 'Abelha', 'bola'] # Ordenação é feita com o código de cada letra. Sendo que as letras maiusculas tem prioridade sobre
# as minusculas. Ordem lexcografica
print(sorted(nomes))