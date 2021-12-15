
class Data:
    # Método construtor:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Método que formata a data:
    def data_fortmatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


