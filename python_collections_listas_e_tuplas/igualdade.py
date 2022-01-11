from python_collections_listas_e_tuplas.conta_corrente import ContaCorrente


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __str__(self):
        return '<<Código: {} Saldo R$ {} >>'.format(self._codigo, self._saldo)


conta1 = ContaSalario(15)
conta1.deposita(1000)
conta2 = ContaCorrente(15)
conta2.deposita(1000)

conta = [conta1 == conta2]
print(conta)

esta = conta1 in [conta2]
print(esta)

estas = conta2 in [conta1]
print(esta)