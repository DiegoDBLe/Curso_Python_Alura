import requests


class AcessoCep:
    def __init__(self, cep):
        if self.cep_eh_valido(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError('CEP inválido!!')

    def __str__(self):
        return self.format_cep()

    def acesso_api_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['cep'],
            dados['logradouro'],
            dados['complemento'],
            dados['localidade'],
            dados['uf']
        )

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
