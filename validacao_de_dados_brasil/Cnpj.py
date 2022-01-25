from validate_docbr import CPF, CNPJ


class Cnpj:

    def __init__(self, documento_cnpj):
        documento_cnpj = str(documento_cnpj)
        if self.cnpj_eh_valido(documento_cnpj):
            self.cnpj = documento_cnpj
        else:
            raise 'CNPJ inválido!!'

    def __str__(self):
        return self.format_cnpj()

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválidos!!')

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
