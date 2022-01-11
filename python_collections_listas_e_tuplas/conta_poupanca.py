
from python_collections_listas_e_tuplas.conta_corrente import ContaCorrente
from python_collections_listas_e_tuplas.heranca_e_polimorfismo import Conta


class ContaPoupanca(Conta):

    def passou_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas:
    conta.passou_o_mes()
    print(conta)