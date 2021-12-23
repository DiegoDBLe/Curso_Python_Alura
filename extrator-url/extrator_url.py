import re


class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL não é valida!')

    def get_url_base(self):
        url_interrogacao = self.url.find('?')
        url_base = self.url[0:url_interrogacao]
        return url_base

    def get_url_parametro(self):
        url_interrogacao = self.url.find('?')
        url_parametro = self.url[url_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_busca = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_busca + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return 'URL: ' + self.url + '\n' + 'Parâmetros: ' + self.get_url_parametro() + '\n' + 'URL Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)

if extrator_url == extrator_url2:
    print('São iguais')
print(f'O tamanho da URL: {len(extrator_url)}')
print(extrator_url)

#print(dir(extrator_url)) # Para saber os métodos e atributos de um objeto.
#valor_quantidade = extrator_url.get_valor_parametro('moedaOrigem')
#print(valor_quantidade)
print()
print()

# ////*****  Desafio *****////
# Conversor de dólar para real
VALOR_DOLAR = 5.50 # 1 Dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversor = int(quantidade) / VALOR_DOLAR
    print(f'O valor de R$ {quantidade} reais é igual a $ {str(valor_conversor)} dolares.')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversor = int(quantidade) * VALOR_DOLAR
    print(f'O valor de $ {quantidade} dólares é igual a R$ {valor_conversor} reais')
else:
    print(f'Cambio de {moeda_origem} para {moeda_destino} não está disponível.')

