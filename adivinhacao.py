print('*' * 33)
print('Bem Vindo ao Jogo de Adivinhação!')
print('*' * 33)

numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while rodada <= total_de_tentativas:
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
    rodada += 1
print('Fim do jogo!')

