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

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self.ano} \nLikes:{self.like}'

    def procurar(self, nome, playlist):
        print(f'{self.nome} tá ou não na lista? ')
        if nome in playlist:
            print('Sim')
        else:
            print('Não')


class Filme(Programa):

    def __init__(self, nome, ano, duracao ):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self.ano} \nDuração: ' \
               f'{self.duracao} minutos \nLikes:{self.like}'


class Series(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self.ano} \nTemporada:' \
               f' {self.temporada} \nLikes:{self.like}'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


# Criando os objetos:
vingadores = Filme('vingadores', 2018, 180)
the_big_bang_theory = Series('the big bang theory', 2015, 6)
todo_mundo_em_panico = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Series('demolidor', 2016, 2)


# Chamando as funções da superclasse:
todo_mundo_em_panico.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
the_big_bang_theory.dar_likes()
the_big_bang_theory.dar_likes()

print('-' * 30)

# Criando uma lista de filmes e series:
filmes_e_series = [vingadores, the_big_bang_theory, demolidor,
                   todo_mundo_em_panico]

# Criar uma playlist:
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


# Obtendo o tamanho da playlist atraves da classe Playlist usando o método
# def __getitem__(self, item):
#         return self._programas[item]
print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')
print('-' * 30)

# Percorrendo a playlist:a
for programa in playlist_fim_de_semana:
    print(programa)
    print('-' * 30)


demolidor.procurar(demolidor, playlist_fim_de_semana)