# https://www.alura.com.br/busca?query=manipulação+de+strings
# “query” é o nome do parâmetro e “manipulação+de+strings” é o valor deste
# parâmetro. A utilização dos símbolos de adição (+) é feita porque não podemos utilizar espaços em branco em URLs. Note que o símbolo “?” não faz parte dos
# parâmetros, pois é apenas o separador: base?parâmetros.

# nossa url é uma string
# url = "http://bytebank.com/cambio?moedaDestino=dolar$moedaOrigem
# =realmoedaDestino=dolar
# &quantidade=100"
# print(url)

#url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100'

url = ''

# Sanitização(limpeza) da URL:
url = url.strip()

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia')

# Localizar a interrogação na string url
url_interrogacao = url.find('?')

# Fatiar a url base
url_base = url[0:url_interrogacao]
print(url_base)

# Fatiar a url parametro
url_parametro = url[url_interrogacao+1:]
print(url_parametro)

# Fatiar até o variavel moedaOrigem:
parametro_busca = 'moedaDestino'
indice_busca = url_parametro.find(parametro_busca)
print(indice_busca)

# Fatiar até a primeira string depois do sinal de =
indice_valor = indice_busca + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)












