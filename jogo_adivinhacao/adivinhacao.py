from random import randint


def jogar():
    print('*' * 33)
    print('Bem Vindo ao Jogo de Adivinhação!')
    print('*' * 33)

    numero_secreto = randint(1, 100)
    total_de_tentativas = 0
    facil = 1
    medio = 2
    dificil = 3
    pontos = 1000

    print(f'Total de Pontos: {pontos}')
    nivel = int(input('Qual nível de dificuldade?\n(1) Fácil (2) Médio (3) '
                      'Difícil: '))

    if nivel == facil:
        total_de_tentativas = 20
    elif nivel == medio:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print()
        print(f'Tentativa {rodada} de {total_de_tentativas}: ')
        chute = int(input('Digite um número entre 1 e 100: '))

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Parabéns!! Você acertou.\nTotal de {pontos} pontos.')
            break
        else:
            if maior:
                print(f'Você errou!! O número {chute} é maior que o número '
                      f'secreto!')
            elif menor:
                print(f'Você errou!! O número {chute} é menor que o número '
                      f'secreto!')
            if rodada == total_de_tentativas:
                print(f'Você excedeu o total de tentativas.\nTotal de {pontos} '
                      'pontos.')
                break
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    print('Fim do jogo!')
    print(numero_secreto)


if __name__ == '__main__':
    jogar()
