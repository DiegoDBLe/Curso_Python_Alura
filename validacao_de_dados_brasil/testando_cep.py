from acesso_cep import AcessoCep
import requests

# Criando um objeto, validando e formatando atraves da classe AcessoCep
cep = 60811110
objeto_cep = AcessoCep(cep)
print(objeto_cep)

# Fazendo a solicitação na API e passando o cep. Retorna o codigo de resposta.
r = requests.get('https://viacep.com.br/ws/60811110/json/')
print(type(r)) # retorna o tipo do objeto
print(dir(r)) # retorna os metodos e atributos que a classe possui.
#print(r.text) # Atributo que mostra as informações do cep informado.

cep_1 = 60192165
objeto1_cep = AcessoCep(cep_1)
print(objeto1_cep.acesso_api_cep())
print()

# .text é o atributo da classe que retorna uma string.
# .json() é o método da classe que retorna um dicionário.
# exemplo:

print(type(r.text))
print(type(r.json()))
print()
print(r.text)
dicionario = dict(r.json())

for i in dicionario.items():
    print(f'{i}')

print(r.json()['bairro'])

print()
print()
bairro, cep_, rua, complemento, cidade, estado,  = objeto_cep.acesso_api_cep()
print(f'Bairro: {bairro}'
      f'\nCep: {cep_}'
      f'\nRua: {rua}'
      f'\nComplemento: {complemento}'
      f'\nCidade: {cidade}'
      f'\nEstado: {estado}')
