# https://www.alura.com.br/busca?query=manipulação+de+strings
#“query” é o nome do parâmetro e “manipulação+de+strings” é o valor deste
# parâmetro. A utilização dos símbolos de adição (+) é feita porque não podemos utilizar espaços em branco em URLs. Note que o símbolo “?” não faz parte dos
# parâmetros, pois é apenas o separador: base?parâmetros.


# Antes da interrogação (?) é chamada de base da url e depois é chamado de
# parametros.

# indicando o domínio: https://
# site: http://bytebank.com
#  indicando que eu estou na página de cambio =  cambio
# Abaixo os parametros:
# indicando que tem uma variavel chamada de moeda origem recebe real:moedaOrigem=real
# (&), que serve para separar esses parâmetros
# outra variavel chamada moeda destino que recebe dolar: moedaDestino=dolar
# (&), que serve para separar esses parâmetros
# outra variavel que recebe a quantidade: quantidade=100

# nossa url é um string
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

url_tamanho = 'bytebank.com/cambio?moedaOrigem=real'
print(f'Tamanho da URL: {len(url)}')

# Abaixo exemplo de fatiamento
url_base = url_tamanho[0:19]
print(url_base)

url_parametro = url_tamanho[20:36]
print(url_parametro)
