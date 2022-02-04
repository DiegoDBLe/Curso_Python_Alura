from tdd.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

# Criando usuario:
gui = Usuario('Gui')
yuri = Usuario('Yuri')

# Instanciando o usuario com um valor ou seja cada usuario deu um lance:
lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

# Informando o produto que será leiloado:
leilao = Leilao('Celular')

# Adicionando os lances do leilão na lista:
leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

# percorrer a lista de lance do leilao:
for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de R$ {lance.valor}')

# Teste avaliador:
avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de R$ {avaliador.menor_lance} e o maior lance foi de R$ {avaliador.maior_lance}')
