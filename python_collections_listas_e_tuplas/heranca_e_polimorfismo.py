from abc import abstractmethod, ABCMeta
from functools import total_ordering


 # Essa função, o total_ordering(), dá para uma classe várias outras comparações, tudo que você tem que fazer é definir o igual, __eq__, e
# o menor, __lt__.O resto ela mesmo define, o menor igual, o maior, o maior igual, será tudo adicionado. Para comparar objetos se são iguais.
@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo  = 0

    def deposita(self, valor):
        self._saldo += valor

    # Função utilizada na class ContaCorrente para verificar se um objeto é menor que o outro no interavel. Nesse caso pelo atributo _saldo
    def __lt__(self, outro): # ls significa menor que.
        if self._saldo != outro._saldo: # Se o saldo for diferente do outro saldo. Ou seja se os saldos forem diferentes compara os saldos.
            return self._saldo < outro._saldo # Função retorna o saldo menor.

        return self._codigo < outro._codigo # Se os saldos forem iguais retorna a comparação dos codigos.

    @abstractmethod
    def passou_o_mes(self):
        pass

    def __str__(self):
        return '[>>Código: {} Saldo R$ {} <<]'.format(self._codigo, self._saldo)


