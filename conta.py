from typing import Any

import datas
from datas import Data


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto...{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de R$ {self.__saldo} do titular: {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def __saldo_disponivel(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__saldo_disponivel(valor):
            self.__saldo -= valor
        else:
            print((f'Saldo insuficiente!!\nSaldo Disponivel R$ '
                   f'{self.__saldo + self.__limite}'))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'Transferencia Realizada com Sucesso!!\nSeu novo saldo é de R$ {self.__saldo}')

    def limite_usado(self):
        if self.__saldo < 0:
             print(f'Você está usando seu limite! R$ {self.__saldo}')

    # Getter atraves de @ anotação
    @property
    def saldo(self):
        if self.limite_usado():
            print()
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # setter atraves de @ anotação
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'ITAU': '341', 'Bradesco': '237'}
