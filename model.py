class Programa:
    def __init__(self, nome, ano, ):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @property
    def like(self):
        return self._like

    def dar_likes(self):
        self._like += 1

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'Nome: {self._nome}'
              f'\nAno: {self.ano}'
              f'\nLikes:{self.like}')


class Filme(Programa):

    def __init__(self, nome, ano, duracao ):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self._nome}'
              f'\nAno: {self.ano}'
              f'\nDuração: {self.duracao} minutos'
              f'\nLikes:{self.like}')


class Series(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def imprime(self):
        print(f'Nome: {self._nome}'
              f'\nAno: {self.ano}'
              f'\nTemporada: {self.temporada}'
              f'\nLikes:{self.like}')


filme = Filme('vingadores', 2018, 180)
filme.dar_likes()

seriado = Series('the big bang theory', 2015, 6)
seriado.dar_likes()
seriado.dar_likes()

print('-' * 30)

filmes_e_series = [filme, seriado]

for programa in filmes_e_series:
    programa.imprime()
    print('-' * 30)
