# Criar duas listas com 4 elementos.
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
print(usuarios_data_science, usuarios_machine_learning)
print()
# Fazendo uma cópia(extend) da lista usuarios_data_science para lista assistiram:
# assistiram = []
# assistiram.extend(usuarios_data_science)
# assistiram

# Fazendo um cópia de lista utilizando o método copy()
assistiram = usuarios_data_science.copy()
print(assistiram)
print()

# juntando as duas listas usuarios_data_science e usuarios_machine_learning em uma unica lista completa com os numeros repetidos.
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print()

# Porém tem dois numeros repetidos.
print(f'Quantos elementos possui a lista assistiram: {len(assistiram)}')
print()
# Para não ter valores repetidos colocamos em um conjunto(set): Não possui elementos repetidos.
print(set(assistiram))
print()

# Tupla ()
# Lista []
# set {} não existe indexização. Ou seja ele não possui indice de acesso.

usuarios_data_science_ = {15, 23, 43, 56}  # Criando um conjunto(set)
usuarios_machine_learning_ = {13, 23, 56, 42}  # Criando outro conjunto(set)

# Unindo os dois conjuntos(set) usando o pip | como se fosse um extend: ele vai juntar os dois conjuntos e excluir os que estão repetidos.
assistiram_ = usuarios_data_science_ | usuarios_machine_learning_  # | significa ou
print(sorted(set(assistiram_)))
print()
for usuario in sorted(assistiram_):
    print(usuario)

print('-' * 30)
print()

for usuario in set(assistiram_):
    print(usuario)

print('-' * 30)
print()
# Operador & e vai verificar o valor que estão em ambas as listas. Ou seja 23 e 56
assistiram_os_dois = usuarios_data_science_ & usuarios_machine_learning_
print(f'Operador & e vai verificar o valor que estão em ambas as listas. Ou seja 23 e 56: {assistiram_os_dois}')

print('-' * 30)
print()

# Operador ^ ou exclusivo vai retornar os numeros que estao no primeiro conjunto e no segundo conjunto e não se repetem.
um_ou_outro = usuarios_data_science_ ^ usuarios_machine_learning_
print(f'Operador ^ ou exclusivo vai retornar os numeros que estao no primeiro conjunto e no segundo conjunto e não se repetem: {um_ou_outro}')

print('-' * 30)
print()

# Elementos que possui na variavel usuarios_data_science_ não repete e não tem na variavel usuarios_machine_learning_
tem_no_ds = usuarios_data_science_ - usuarios_machine_learning_
print(tem_no_ds)

print('-' * 30)
print()

# mesma coisa da operação acima;
tem_no_ml = usuarios_machine_learning_ - usuarios_data_science_
print(tem_no_ml)

# O que são conjuntos;
# Criar conjuntos;
# Utilizar o | para juntar conjuntos;
# Utilizar o & para juntar apenas números que estão no mesmo conjunto;
# Utilizar o - para remover números repetidos que estão no em dois conjuntos;
# O que é ou (^) exclusivo.
print('-' * 30)
print()
print()

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(f'Tipo: {type(usuarios)}')
print(f'Tamanho: {len(usuarios)} elementos.')
# Conjunto no python é mutavel e o metodo add() adiciona elementos no set(). Porem se ja tiver um valor igual no conjunto ele nao adiciona:
usuarios.add(765)
print(f'Novo tamanho: {len(usuarios)} elementos. {usuarios}')

print()

# Se eu quiser deixar um conjunto imutavel, eu faço o congelamento(frozenset) dele:
usuarios = frozenset(usuarios)
print(f'Tipo, após fazer o congelamento: {type(usuarios)}')

print()

# Conjunto(set) pode ser com string's:
meu_texto = 'Bem vindo meu nome é Diego eu gosto muito de nomes e tenho um cachorro e gosto muito de cachorro'
# Usar o método slipt() para quebrar os espaços em branco do texto, por padrao ele quebra os espaços em branco.
print(f'Usando o método slipt():\n{meu_texto.split()}')  # vai retornar uma lista.

print()

# Transformando meu texto em um conjunto. Transformando meu texto em conjunto as palavras repetidas nao aparecerão. tirando a duplicidade
print(f'Transformando meu texto em um conjunto(set),quebrando os espaços em branco e titrando os elementos repetidos: \n{set(meu_texto.split())}')

print()

# Criando um Diciónario:
aparicoes = {
    'Diego': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}
print(f'Tipo: {type(aparicoes)}')
print(f'# Qual o valor da chave Diego: {aparicoes["Diego"]}')
print(f'# Qual o valor da chave Cachorro: {aparicoes["cachorro"]}')
# Qual o valor da chave 'xpto' uma chave que não está em aparicoes(dicionario): vai aprasentar erro, pois chave não existe no dicionario.
# Para nao apresentar erro, usa o método get() e passa como parametro o valor 0. Para as chaves que não existirem no dicionario ele vai retornar o valor 0
print(f'# Qual o valor da chave Xpto(Chave inexistente) no conjutno: {aparicoes.get("Xpto", 0)}')
print()
# Outra maneira de criar um dicionario seria instanciando o construtor do dicionario:
aparicoes_ = dict(Diego=1, cachorro=2, uva=10)
print(f'Tipo: {type(aparicoes_)}')
print(f'Tamanho: {len(aparicoes_)}')
print(f'# Qual o valor da chave Cachorro: {aparicoes_["cachorro"]}')
print(f'# Qual o valor da chave Uva: {aparicoes_["uva"]}')
print(f'# Qual o valor da (Chave inexistente) no conjutno: {aparicoes.get("banana", 0)}')
print('-' * 30)
print()
# Criando um dicionario:
frutas = {
    'Banana': 2,
    'Uva': 8,
    'Melancia': 5
}
print(f'Criando: \n{frutas}')
# Adicionando chaves e valores no meu dicionario:
frutas['Maracuja'] = 2
print(f'Adicionando:\n{frutas}')
frutas['Laranja'] = 10
print(f'Adicionando:\n{frutas}')
# Substituindo o valor de uma chave no dicionario:
frutas['Banana'] = 12
print(f'Substituindo: \n{frutas}')
del frutas['Maracuja']
print(f'Removendo: \n{frutas}')
print()

# Verificando se possui determinada chave no dicionario:
banana = 'Banana' in frutas
print(banana)

maracuja = 'Maracuja' in frutas
print(maracuja)

print(f'get: {frutas.get("Uva")}')
print()

# Fazer uma iteração no dicionario: Por padrão aparece somente as chaves:
for fruta in frutas:
    print(fruta)
print()

# Igualmente o padrão retorna somente as chaves.
for fruta in frutas.keys():
    print(fruta)
print()

# Fazendo um for pelas chaves e pegando somente os valores de cada chave:
for fruta in frutas.values():
    print(fruta)
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 1° Maneira e mais 'grosseira':
for fruta in frutas:
    print(fruta, frutas[fruta])
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 2° Maneira e mais 'grosseira'tbm:
for fruta in frutas:
    valor = frutas[fruta]
    print(fruta, valor)
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 3° Maneira e mais comum: utilizando o método items()
for fruta in frutas.items():
    print(fruta)
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 4° Maneira e mais comum: utilizando o método unpack(desempacotamento)
for chave, valor in frutas.items():
    print(f'Chave: {chave} - valor: {valor}')
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 5° Maneira e mais elegante: utilizando o método list comprehension e colocando o nome
# nas chaves
print(['Chave: {}'.format(chave) for chave in aparicoes.keys()])
print()

# Fazendo um for pelas chaves e valores: Passando por linha a linha. 5° Maneira e mais elegante: utilizando o método list comprehension e colocando o
# nome nos valores
print(['Valor: {}'.format(valor) for valor in aparicoes.values()])

print()
# Fazendo um for pelas chaves e valores: Passando por linha a linha. 5° Maneira e mais elegante: utilizando o método list comprehension e colocando os
# nomes nas chaves e valores.
print(['Chave: {} - Valor: {}'.format(chave, valor) for chave, valor in frutas.items()])


# O que aprendemos nesta aula:
#
# O que é um dicionário;
# Verificar se o elemento está dentro do dicionário;
# Utilizar o get para verificação;
# Criar um dicionário a partir do dict;
# Adicionar um elemento no dicionário;
# Remover um elemento do dicionário;
# Mostrar os elementos dentro do dicionário;
# Usar a função keys para pegar as chaves;
# Usar a função values para pegar os valores;
# Percorrer linha a linha com a função items.

print('-' * 120)
print()
# Pegando uma string, tranformando em uma lista, passeando em uma lista com o for, e jogando pedaços dela em um diciónario de acordo com o que foi solicitado.
# Transformando todo o texto em minusculo.
meu_texto = meu_texto.lower()
print(meu_texto)

# Criando um dicionario vázio para colocar cada palavra e quantas vezes apareceu dentro do dicionario.
_aparicoes_ = {}

# passando por cada palavra e Quebrando as palavras.
for palavra in meu_texto.split():
    ate_agora = _aparicoes_.get(palavra, 0)  # se a palavra estiver em aparicoes e conta e soma mais um, se nao tiver ele coloca 0
    _aparicoes_[palavra] = ate_agora + 1 # Somando +1 para se aparecer mais q uma vez ir contando quantas vezes apareceu
for palavra in _aparicoes_.items():
    print(palavra)
print('-' * 120)
print()
# mesma versão da de cima, porém usando defaultdict que é colocando o valor da chave padrão em 0:
from collections import defaultdict

_aparicoes_ = defaultdict(int) # Passa int como parâmetro por padrao o valor de int é 0. Então se for passada uma chave inexistente retorna 0
# passando por cada palavra e Quebrando as palavras.

for palavra in meu_texto.split():
    ate_agora = _aparicoes_[palavra] # usando o  defaultdict(int) não precisa do get
    _aparicoes_[palavra] = ate_agora + 1
print(_aparicoes_)
print()

# Simplificando o codigo:

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  aparicoes[palavra] += 1
print(aparicoes)
print()

# Importando a biblioteca:
from collections import Counter

# Simplificando o codigo usando o método Counter:

aparicoes = Counter(meu_texto.split())
print(f'Simplificando o codigo usando o método Counter: {aparicoes}')



