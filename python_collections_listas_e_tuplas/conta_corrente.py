

from python_collections_listas_e_tuplas.heranca_e_polimorfismo import Conta


class ContaCorrente(Conta):

    def passou_o_mes(self):
        self._saldo -= 2

# Ordenação de objetos:


def extrai_saldos(conta):
    return conta._saldo


conta_diego = ContaCorrente(18)
conta_diego.deposita(500)

conta_levi = ContaCorrente(27)
conta_levi.deposita(1000)

conta_thyci = ContaCorrente(28)
conta_thyci.deposita(510)

contas = [conta_levi, conta_thyci, conta_diego]
for conta in contas:
    print(conta)

print('-' * 30)

# Acessando o atributo para comparação Usando a função extrai_saldos. mas tem algo muito feio aqui que doeu meu coração, deve ter doído no seu também.
# Dentro da função extrai_saldo, eu acessei um atributo  que era para ser privado, eu acessei com o underline, coisa muito feia.
for conta in sorted(contas, key=extrai_saldos):
    print(conta)
print()
print('-' * 30)
# Outra forma deacessar o atributo de uma lista para comparação sem a criação de uma função:
# Estamos usando um tributo e podemos ordenar dizendo que a chave é uma attrgetter(“_saldo”)
#Não precisamos criar essa função se só queremos acessar um atributo, fosse um atributo público ou não, ou com underline. Então, é uma outra maneira,
# sem precisar criar uma função customizada, um lambda, seja lá o que for, eu posso ir direto chamar o attrgetter. Vamos ver o resultado? O resultado é
# ordenado, as contas estão ordenadas pelo saldo. Porém, continuo acessando um atributo privado
from operator import attrgetter
# Interando e colocando em ordem crescente pelo codigo da conta:
for codigo in sorted(contas, key=attrgetter('_codigo')):
    print(codigo)
print()
print('-' * 30)
# Interando e colocando em ordem crescente pelo saldo da conta:
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)
print()
print('-' * 30)
# Ordem crescente interavel de uma lista de objetos ordenando pelo atributo _saldo.
for conta in sorted(contas):
    print(conta)

maior = conta_diego > conta_levi
if maior:
    print(f'A conta {conta_levi} É maior! que a conta {conta_diego}')
else:
    print(f'A conta {conta_diego} É menor! que a conta {conta_levi}')
print()
print('-' * 30)
# ordem decrescente iteravel de uma lista de objetos ordenando pelo atributo _saldo.
for conta in sorted(contas, reverse=True):
    print(conta)
print()
print('-' * 30)

# Agora vamos desempatar. Por exemplo se duas contas tem o mesmo valor de saldo, vamos colocar outro criterio de desempate.
conta_mauro = ContaCorrente(1963)
conta_mauro.deposita(600)

conta_marina = ContaCorrente(600)
conta_marina.deposita(600)

conta_sergio = ContaCorrente(100)
conta_sergio.deposita(600)

conta_dinha = ContaCorrente(32)
conta_dinha.deposita(600)

contas2 = [conta_mauro, conta_sergio, conta_marina, conta_dinha]
for conta in sorted(contas2, key=attrgetter('_saldo', '_codigo')): # No attrgetter posso passar outro parametro para desempatar caso o primeiro
    # parametro seja igual.
    print(conta)
print()
print('-' * 30)

# Orientação a objeto: Agora comparação entre dois objetos para desempatar: tenho que fazer uma implementação na def lt(maior que) na classe Conta:
# Não precisa usar a classe attrgetter, pois foi implementado na def de forma natural. Quando os saldos sao iguais vai procurar pelo codigo.
for conta in sorted(contas2):
    print(conta)
print()
print('-' * 30)
# Com anotação @total_ordering na classe Conta, podemos verificar se uma conta é igual a outra, maior, ou menor ou igual a propria conta. Atraves dessa
# anotação, que para funcionar tem que ser implantada na classe Conta duas funções: igualdade(eq) e menor que(lt).
igual = conta_diego == conta_diego
print(igual)