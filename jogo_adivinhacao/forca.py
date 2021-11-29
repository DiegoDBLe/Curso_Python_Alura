
def jogar():
    print('*' * 33)
    print('   Bem Vindo ao Jogo de Forca!')
    print('*' * 33)

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou  = False

    print(f'A palavra contém {len(letras_acertadas)} letras: {letras_acertadas}')

    while not enforcou and not acertou:

        chute = str(input('Digite uma letra: ')).strip().lower()
        print('jogando...')

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1
        print(f'{letras_acertadas} faltam {letras_acertadas.count("_")} '
              f'letras.')
        if letras_acertadas.count('_') == 0:
            print(f'Parabéns você acertou a palavra é'
                  f' {palavra_secreta.upper()}!')
            break


if __name__ == '__main__':
    jogar()