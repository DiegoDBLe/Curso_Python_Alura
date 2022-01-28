from datetime import datetime, timedelta
from datas_br import DatasBr

# Retorna o ano/mes/dia e a hora:minutos:segundos
print(datetime.today())

# Retorna o ano/mes/dia e a hora:minutos:segundos Utilizando o método da classe DatasBr, que na hora que faz o cadastro já registra o horario e data.
cadastro = DatasBr()
print(cadastro.momento_cadastro)

# Utilizando o método que retorna o mês do cadastro: utilizando o método month da classe datetime ele retorna um numero inteiro.
# Criei uma variavel e passei uma lista com os messes do ano, e retornei a variavel com o indice que o método month retorna.
mes_cadastro = DatasBr()
print(mes_cadastro.mes_do_cadastro())

# Utilizando o método que retorna os dias da semana weekday() da biblioteca datime ele também retorna um numero inteiro, criei uma vairavel onde passei
# uma lista com os dias da semana, e depois essa variavel da lista recebe como parametro a variavel onde esta o método weekday().
dia_do_cadastro = DatasBr()
print(dia_do_cadastro.dia_do_cadastro())

# Formatando data e hora:
hoje = datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('Data: %d/%m/%Y Hora: %H:%M')
print(hoje_formatado)
print()

# Instanciando um objeto:
data = DatasBr()
print(data)
print()

# Quanto tempo o usuario fez o cadastro utilizando o timedelta():
hoje_ = datetime.today()
amanha = datetime.today() + timedelta(days=1)
print(amanha - hoje_)

# Testando o metodo tempo_de_cadastro() da classe datas_br:
hoje_1 = DatasBr()
print(hoje_1.tempo_de_cadastro())
