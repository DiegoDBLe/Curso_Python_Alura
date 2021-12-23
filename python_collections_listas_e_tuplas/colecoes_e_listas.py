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

# Adicionar elementos na lista:
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

# Inserir um elemento em uma posição (local) especifico:
idades.insert(0, 20)
print(idades)

# Adicionar vários elementos em uma lista:
idades.extend([20, 19, 44])
print(idades)

# 