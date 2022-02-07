from tdd.src.leilao.dominio import Usuario, Leilao

import pytest

# Com o Pytest não conseguiremos usar o método setUp() usando funções da mesma forma que fizemos no "test_leilao.py". Nesse momento, trabalharemos de
# forma diferente. Já comentamos que se costuma chamar de fixture o que for necessário para a criação e funcionamento de teste. Então, vamos decorar o
# método, avisando o Pytest que a função vini() é uma fixture, escrevendo pytest.fixture() antes dela.
from tdd.src.leilao.excecoes import LanceInvalido


@pytest.fixture
def vini():
    return Usuario('vini', 100.0)


@pytest.fixture()
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini, leilao):
    #diego = Usuario('Diego', 100.0)

    #leilao = Leilao('Celular')

    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):

    #levi = Usuario('Levi', 100.00)

    #leilao = Leilao('Celular')

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_do_que_o_da_carteira(vini, leilao):
    # Lançando excessão: Quando o codigo tem que apresentar uma exceção e para passar no teste, quando tiver excessao mostre.
    with pytest.raises(LanceInvalido):

        #diego = Usuario('Diego', 100.0)

        #leilao = Leilao('Celular')

        vini.propoe_lance(leilao, 200.0)

        #assert diego.carteira == 100
