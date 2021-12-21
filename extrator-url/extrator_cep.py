# Expressões regulares

endereco = 'Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, ' \
           'RJ, 23440-120'

import re # Regular Expression -- RegEx

# padrao de um cep é assim: tem 5 digitos, tem um hifen(opcional) + 3 digitos:

# 5 grupos de digitos, hifen + 3 grupos de digitos que podem ser de 0 ate 9
# método compile é uma maneira de criar um padrão.
#padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]') # O interrogação é para que
# quando o cep for passado sem o hifen ele seja localizado tbm.

# Simplificando a variavel padrao utilizando quantificadores:
# quantificadores para dizer quantas vezes um certo conjunto aparece naquele padrão.
padrao = re.compile('[0-9]{5}[-]?[0123456789]{3}')


# Buscar na string se esse padrao foi encontrado:
busca = padrao.search(endereco) # caso o padrao seja encontrado ele retorna Match, caso o padrão não seja encontrado ele retorna none.
if busca:
    cep = busca.group()
    print(cep)
