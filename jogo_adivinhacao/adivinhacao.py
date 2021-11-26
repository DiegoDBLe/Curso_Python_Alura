print('*' * 33)
print('Bem Vindo ao Jogo de Adivinhação!')
print('*' * 33)

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}: ')
    chute = int(input('Digite seu número: '))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print('Parabéns!! Você acertou.')
        break
    else:
        if maior:
            print(f'Você errou o número {chute} é maior que o número secreto!')
        elif menor:
            print(f'Você errou o número {chute} é menor que o número secreto!')
        if rodada == 3:
            print('Você excedeu o total de tentativas.')
            break
print('Fim do jogo!')

