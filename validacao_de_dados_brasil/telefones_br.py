import re


class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número inválido!!')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        # xxx (xx)xxxx-xxxx  (codigo do pais) (codigo de area estado) (final do telefone)
        padrao_telefone = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao_telefone, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao_telefone = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        separar = re.search(padrao_telefone, self.numero)
        numero_formatado = f'+{separar.group(1)}' \
                           f'({separar.group(2)})' \
                           f'{separar.group(3)}-{separar.group(4)}'
        return numero_formatado
