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


extrator_url = ExtratorURL('bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')
valor_quantidade = extrator_url.get_valor_parametro('moedaOrigem')
print(valor_quantidade)
