

def criar_conta(numero, titular, saldo, limite):
    conta2 = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta2


def depositar(conta, valor):
    conta['saldo'] += valor


def sacar(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'Saldo é R$ {conta["saldo"]}')
