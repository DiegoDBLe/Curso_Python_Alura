idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1, idade2, idade3, idade4)

# Criando e imprimindo uma lista
idades = [39, 30, 27, 18]
print(idades)

# Tamanho de uma lista:
print(len(idades))

# Adicionar elementos na lista: o append adiciona um elemento no final da lista.
idades.append(15)
print(idades)

# Percorrer uma lista:
for idade in idades:
    print(idade)

# Remove um elemento da lista:
idades.remove(39)
print(idades)

# Colocando a lista em ordem crescente
print(sorted(idades))

# Para saber se um determinado elemento está na lista ou não:
print(15 in idades, f': O número {15} está na lista')
print(20 in idades, f': O número {20} não está na lista')

# Inserir um elemento na posição(local) desejado especifico:
idades.insert(0, 20)
print(idades)
idades.insert(2, 22)
print(idades)

# Adicionar vários elementos em uma lista: estende a lista com quantos numeros eu desejar.
idades.extend([20, 19, 44])
print(idades)

# Idades com um ano a mais:
# Pode ser feito um for adicionando o número 1 ou  criando uma lista vazia:
# for idade in idades:
#     print(idade + 1)

# Idade ano que vem:

# idades_ano_que_vem = []
# for idade in idades:
#     idades_ano_que_vem.append(idade + 1)
# print(idades_ano_que_vem)

# Outra sintaxe para fazer a mesma coisa:

idades_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_ano_que_vem)

# maiores que 21 em uma unica linha:

maiores_de_vinte_e_um = [idade for idade in idades if idade > 21]
print(maiores_de_vinte_e_um)


def proximo_ano(idade):
    return idade + 1


maior_de_vinte = [proximo_ano(idade) for idade in idades if idade > 21]
print(maior_de_vinte)


# Lista como parametro é uma boa pratica passar o valor com default None(nada).
def faz_processamento(lista=None):
    if lista is None: # Se a lista é nada(vaizia)
        lista = list() # cria uma nova lista vazia.
    lista.append(13) # Caso contrario adiciona o valor 13
    print(len(lista)) # Tamanho da lista


iDade = [16, 21, 29, 56, 43]
faz_processamento(iDade)
print(iDade)

print(sorted(idades))
idades.remove(20)
print(sorted(idades))
