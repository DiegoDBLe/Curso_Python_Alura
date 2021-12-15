# https://www.alura.com.br/busca?query=manipulação+de+strings
#“query” é o nome do parâmetro e “manipulação+de+strings” é o valor deste
# parâmetro. A utilização dos símbolos de adição (+) é feita porque não podemos utilizar espaços em branco em URLs. Note que o símbolo “?” não faz parte dos
# parâmetros, pois é apenas o separador: base?parâmetros.

# nossa url é uma string
#url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar
# &quantidade=100"
#print(url)

url = 'http://bytebank.com/cambio?moedaOrigem=real'
print(f'URL: {url}')

interrogacao = url.find('?')
url_base = url[0:interrogacao]
print(f'URL base: {url_base}')

url_parametro = url[interrogacao+1:]
print(f'URL parametro: {url_parametro}')
