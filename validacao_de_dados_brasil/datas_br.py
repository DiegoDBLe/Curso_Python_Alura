from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_do_cadastro(self):
        meses_do_ano = ['Janeiro', 'Fevereiro', 'Março',
                        'Abril', 'Maio', 'Junho',
                        'Julho', 'Agosto', 'Setembro',
                        'Outubro', 'Novembro', 'Dezembro']
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_do_cadastro(self):
        dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                          'Quinta-feira', 'Sexta-feira', 'Sabádo', 'Domingo']
        dia_do_cadastro = self.momento_cadastro.weekday()
        return dias_da_semana[dia_do_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('Data: %d/%m/%Y Hora: %H:%M')
        return data_formatada

    def tempo_de_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
