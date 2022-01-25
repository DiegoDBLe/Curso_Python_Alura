# Factory: Fica responsavel por chamar a classe certa que o nosso objeto precisa, ou seja se eu passar para a factory o cnpj ela vai chamar a classe
# CNPJ, se eu passar para factory um cpf ela vai chamar um a classe cpf. Correto! Para conseguirmos usar qualquer instância retornada pelo Factory
# livremente, os métodos das classes filhas precisam ser iguais. A nova classe precisará ter todos os métodos com os mesmos nomes das outras classes filhas.
from validate_docbr import CPF, CNPJ, CNH


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de digitos está incorreta!')


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf inválido!!')

    def __str__(self):
        return self.format(self.cpf)

    def valida(self, documento):
        valida_cpf = CPF()
        return valida_cpf.validate(documento)

    def format(self, documento):
        mascara = CPF()
        return mascara.mask(documento)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('Cnpj inválido!!')

    def __str__(self):
        return self.format(self.cnpj)

    def valida(self, documento):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(documento)

    def format(self, cnpj):
        mascara = CNPJ()
        return mascara.mask(cnpj)


class DocCnh:

    def __init__(self, documento):
        if self.valiada(documento):
            self.cnh = documento
        else:
            raise ValueError('CNH inválido!!')

    def __str__(self):
        return self.format(self.cnh)

    def valiada(self, documento):
        valida_cnh = CNH()
        return valida_cnh.validate(documento)

    def format(self, cnh):
        mascara = CNH()
        return mascara.mask(cnh)
