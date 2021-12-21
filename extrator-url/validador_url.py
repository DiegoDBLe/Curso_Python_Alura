'''Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs válidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''

#RegEx vai seguir três passos, que são: compilar um padrão, comparar esse padrão com uma string e verificar se isso retornou alguma combinação, se esse
# padrão foi encontrado.
# Padrão: https://www.bytebank.com.br/cambio

import re

url = 'https://www.bytebank.com.br/cambio'

# Quando utilizamos colchetes, por exemplo, [abc], eu estou dizendo que esse conjunto da minha expressão regular pode ter qualquer um desses caracteres
# aqui dentro, ou pode ser ‘a’ ou pode ser ‘b’ ou pode ser ‘c’.
#Quando eu utilizo parênteses, eu estou falando que aquele conjunto tem que ser exatamente aqueles caracteres, ou seja, se eu coloco (abc), a nossa string
# a ser comparada com o padrão teria que possuir exatamente ‘abc’ e não só um desses caracteres. Estamos utilizando parênteses porque eu estou falando:
# “Ele tem que começar com https”.
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A URL não é valida!')
else:
    print('URL é válida!')