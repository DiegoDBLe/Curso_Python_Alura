class ContaCorrente_:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor} realizado com sucesso!')

    def __str__(self):
        return '[>> Código: {} Saldo R$ {} <<]'.format(self.codigo, self.saldo)


conta_do_diego = ContaCorrente_(15)
print(conta_do_diego)

conta_do_diego.deposita(500)
print(conta_do_diego)

print()

conta_do_levi = ContaCorrente_(47685)
conta_do_levi.deposita(1000)
print(conta_do_levi)

print()

conta_da_thyci = ContaCorrente_(123)
conta_da_thyci.deposita(800)
print(conta_da_thyci)
print()

conta = [conta_do_diego, conta_do_levi, conta_da_thyci]
for contas in conta:
    print(contas)

print()
conta[2].deposita(100)
print(conta[2])
print()
conta_da_thyci.deposita(100)
print(conta_da_thyci)

print()
print()
print('Tuplas: ')  # Imutável


def deposita_para_todas(contass):
    for conta in contas:
        conta.deposita(100)
        print(conta)


contas = [conta_do_diego, conta_do_levi, conta_da_thyci]
deposita_para_todas(contas)
# contas.insert(0, 76)
print(contas[0], contas[1], contas[2])
deposita_para_todas(contas)

print()

conta_familia = (15, 1000)
print(conta_familia)


def depositar(conta, valor):
    novo_saldo = conta[1] + valor
    codigo = conta[0]
    return (codigo, novo_saldo)


print(f'Primeiro conta familia: R$ {conta_familia}')
conta_familia = depositar(conta_familia, 100)
print(f'Atribuindo a conta familia com a função: R$ {conta_familia}')
print()

# Misturando Lista e Tupla:
print('Misturando Lista e Tupla:')
diego = ('Diego', 33, 1988)
levi = ('Levi', 2, 2020)
thyci = ('Thycianne', 33, 1988)

usuarios = [diego, levi, thyci]
print(usuarios)
usuarios.append(('Max', 13, 2009))
print(usuarios)
print(f'Quantos usuarios tenho cadastrados: {len(usuarios)}')
print(f'Acessando o primeiro cadastrado da lista: {usuarios[0]}')
usuarios.insert(0, ('Geleia', 4, 2018))
print(usuarios)
usuarios.extend([('Mauro', 58, 1964), ('Marina', 56, 1966)])
print(usuarios)
usuarios.pop(0)
print(usuarios)