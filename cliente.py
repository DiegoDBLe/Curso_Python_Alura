
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('testando anotação @property')
        return self.__nome.capitalize()
