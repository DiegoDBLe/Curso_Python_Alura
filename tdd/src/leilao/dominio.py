# Test Driven Development(Desenvolvimento Orientado por Testes):
import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise ValueError('Saldo na carteira insuficiente para propor um lance!')
        lance = Lance(self, valor)
        leilao.propoe_lance(lance)

        self.__carteira -= valor

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    # Essa classe é para adicionar os lances na lista sem a necessidade de furar o encapsulamento. Ou seja se na hora de adicionar eu colocar o append
    # estou furando o encapsulamento. Então coloco o método append no método propoe_lance. Verificar qual o maior e o menor lance também
    def propoe_lance(self, lance: Lance):
        ''' -> Se a lista de leiloes estiver vazia ou se o usuario do ultimo lance for diferente do usario atual e se o valor do lance proposto for maior
        que o lance do ultimo usuario '''
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance.')

    @property
    def lances(self):
        # Um jeito de limitar será devolver uma cópia da lista. Em vez de devolver a mesma referência para a memória da lista, devolveremos uma cópia.
        # Há muitas formas de fazer cópias de listas no Python, um deles é colocar colchetes e dois pontos [:]
        return self.__lances[:]


'''class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def avalia(self, leilao: Leilao):

        for lance in leilao.lances:
                if lance.valor > self.maior_lance:
                    self.maior_lance = lance.valor
                if lance.valor < self.menor_lance:
                    self.menor_lance = lance.valor
A importancia da class Avaliador: ser separada da classe Leilao.
Esse avaliador checa os valores dos lances do leilão para saber qual será o valor do maior e do menor lance. Já nos perguntamos em outros momentos se faz 
sentido que esse comportamento esteja numa classe separada ou se ele deverá ficar na classe Leilao, para o leilão reconhecer qual o maior e o menor lance.'''