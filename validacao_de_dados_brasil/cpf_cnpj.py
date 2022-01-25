from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, documento, tipo_documento):

        self.tipo_documento = tipo_documento

        documento = str(documento) # Sobrescrevendo o numero que sera passado por paramentro para que o phyton leia como str

        if self.tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento): # Se o documento passado por paramentro tiver 11 caracteres é um cpf válido
                self.cpf = documento
            else:
                raise ValueError('CPF inválido!!')
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido!!')
        else:
            raise ValueError('Documento Inválido!!')

    # Representação String da classe:
    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()

    # Função para verificar se o documento(cpf) tem 11 caracteres. Essa função válida o tamnho do cpf.
    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de digitos inválida!!')

    # Mascara do CPF. Formatado:
    # def format_cpf(self):
    #     fatia_um = self.cpf[:3]
    #     fatia_dois = self.cpf[3:6]
    #     fatia_tres = self.cpf[6:9]
    #     fatia_quatro = self.cpf[9:]
    #     return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'

    # Usando a mscara do proprioa cpacote:
    def format_cpf(self):
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)

    def format_cnpj(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida!!')
