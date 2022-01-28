# As expressões regulares servem para encontrar padrões bem definidos dentro de uma cadeia de caracteres em um texto ou str maiores. Por exemplo,
# se temos um e-mail com um volume textual enorme contendo um número de telefone específico, poderemos extraí-lo sem precisarmos ler todo o conteúdo.
# Para construirmos este padrão, o primeiro passo é conhecer os caracteres especiais da linguagem e saber qual é a biblioteca responsável por isso:
# Os colchetes [] são caracteres especiais: Que definem um range ou um grupo de caracteres, como [0-9], [a-z] ou [abc] por exemplo;
# Já o * pega uma ou mais ocorrências do padrão definido anteriormente;
# As chaves {} nos permitem: definir uma quantidade específica de vezes que queremos que o padrão se repita ou um intervalo de possibilidades,
# como [abc]{5} por exemplo;
# O \w pode ser qualquer número de zero a nove ou letra de "A" a "Z";
# A barra | representa uma coisa ou outra como em @|$ por exemplo;
# Os parênteses () capturam um grupo, e veremos sua importância mais adiante.


# 1° Passo importar a biblioteca de expressoes regulares:
import re

# Criando um padrão que encontra numero, letra e numero: Não pode conter espaços entre um colchete e outro
padrao = '[0-9][a-z][0-9]'

# Criando um texto onde vamos procurar o padrão definido na variavel acima:
texto = '123 1a2 1cc aal blabla meme mimi momo mumu'

# Variavel que vai receber o método de search(buscar) que recebe como parametro as variaveis onde esta o padrao e a variavel onde tem o texto:
buscar = re.search(padrao, texto)
print(buscar.group())

# Procurando um padrao de email dentro de um texto:
# Criando o padrão: \w -> localiza tanto letras quanto numeros. Chaves para dizer quantidade minima de caractere e maxima ate o @. De 3 a 10 é o dominio
padrao_ponto_com = '\w{5,50}@\w{3,10}.\w{2,3}'
email = 'Meu email é deigo_batista@hotmail.com sempre uso ele para receber emails. Tenho tambem outro email diegodantas.batista@gmail.com.br'
localizar = re.search(padrao_ponto_com, email)
print(localizar.group())

padrao_ponto_com_br = '\w{5,50}@\w{3,10}.\w{2,3}.{2,3}'
localiza_br = re.findall(padrao_ponto_com_br, email) # metodo findall localiza todos com o mesmo padrao dentro do texto.
print(localiza_br)
print()

# Localizar um telefone dentro atraves do seu padrao dentro de um texto:
# Padrao do telefone: (xx)xxxx-xxxx as chaves indica quantas repetições tem que ter. No exemplo são dois digitos de codigo de area, ou seja,
# dois numeros entre 0 e 9. Na segunda parte devemos ter de 0 a 9 de 4(se fora celular) a 5(se for residencial) digitos.
padrao_telefone = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto_telefone = 'Eu gosto do numero 8532641000 e do numero 85998285357 tambem'
localiza_telefone = re.findall(padrao_telefone, texto_telefone)
print(localiza_telefone)
print()

# Testando a classe telefones_br
from telefones_br import TelefonesBr

telefone = '558832645051'
tele_objeto = TelefonesBr(telefone)

# Testando  o caractere especial () captura e agrupa que separa em grupos o padrao. Usando o findall() vai retornar uma tupla dos grupos separados
# dentro de uma lista
padrao_telefone = '([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})'
procura = re.findall(padrao_telefone, telefone)
print(procura)

# Usando o método search: retorna o padrao completo.
padrao_telefone = '([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})'
procura = re.search(padrao_telefone, telefone)
print(procura.group())

# Usando o método search passando as posições como parametro no group(): retorna a posição de cada grupo passado no parametro.
padrao_telefone = '([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})'
procura = re.search(padrao_telefone, telefone)
print('+',procura.group(1), '',procura.group(2),procura.group(3),'-',procura.group(4))

print(f'+{procura.group(1)}({procura.group(2)}){procura.group(3)}-{procura.group(4)}')

# Usando o método search passando as posições como parametro no group() e utilizando o caractere especial ?: Que siginifica que aquele grupo onde tem a
# ? não é obrigatorio o preechimento.
# no parametro.
telefone_1 = '8832645051'
padrao_telefone = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
procura = re.search(padrao_telefone, telefone_1)
print('+',procura.group(1), '',procura.group(2),procura.group(3),'-',procura.group(4))
# Não precisa passar o codigo de area, passando ou não ele válida por conta do ?
print(f'{procura.group()}')
print()

# Instanciando um objeto e Utilizando o método format da classe telefones_br:
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
