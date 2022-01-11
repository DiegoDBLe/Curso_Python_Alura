from python_collections_listas_e_tuplas.heranca_e_polimorfismo import Conta

# Não consigo instanciar da class Conta, pois a class Conta está como abstrata e
# não estou utilizando a def passou_o_mes(self):


class ContaInvestimento(Conta):
    pass


investimento = ContaInvestimento(746)
investimento.deposita(1000)
print(investimento)




