from unittest import TestCase

from tdd.src.leilao.dominio import Usuario, Lance, Leilao


# Os nomes das funções testadas devem ser bem calaros.
from tdd.src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    # Podemos isolar esse código através do método setUp que é herdado da classe TestCase. Esse método é invocado antes de cada método de testes, dessa
    # forma, garante que um teste não influencie outro. Alternativa correta! Através do método setUp, conseguimos criar os objetos utilizados pelos testes.
    # Esse método é executado antes de cada teste, dessa forma, garantimos que um teste não influencia outro, já que sempre teremos novos objetos.
    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(lance_do_yuri)
        self.leilao.propoe_lance(self.lance_do_gui)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe_lance(self.lance_do_gui)
            self.leilao.propoe_lance(lance_do_yuri)

    # Após adicionar uma nova regra de negocio essa função perdeu sua utilidade.
    # '''def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
    #     yuri = Usuario('Yuri')
    #     lance_do_yuri = Lance(yuri, 100.0)
    #
    #     self.leilao.propoe_lance(self.lance_do_gui)
    #     self.leilao.propoe_lance(lance_do_yuri)
    #
    #     menor_valor_esperado = 100
    #     maior_valor_esperado = 150
    #
    #     self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
    #     self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)'''

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe_lance(self.lance_do_gui)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        diego = Usuario('Diego', 500.0)
        yuri = Usuario('Yuri', 500.0)

        lance_do_diego = Lance(diego, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(lance_do_yuri)
        self.leilao.propoe_lance(lance_do_diego)

        maior_valor_esperado = 200
        menor_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilão não tiver lances, deve permitir propor um lance.
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe_lance(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)  # Tamanho da lista de lances deve ter pelo menos 1 lance.

    # se o ultimo usuario for diferente, deve permitir propor o lance.
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200)

        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_do_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    # se o ultimo usuario for o mesmo, não deve permitir propor o lance.
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe_lance(self.lance_do_gui)
            self.leilao.propoe_lance(lance_do_gui200)
