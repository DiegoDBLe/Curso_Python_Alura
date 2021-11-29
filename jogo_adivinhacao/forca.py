
def jogar():
    print('*' * 33)
    print('   Bem Vindo ao Jogo de Forca!')
    print('*' * 33)

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou  = False
    tentativa = 1
    contador  = 0

    print(f'A palavra contém {len(letras_acertadas)} letras: {letras_acertadas}')

    while not enforcou and not acertou:
        contador += 1
        if contador == 10:
            print(f'Encerrando o jogo... Após {contador} tentativas.')
            break
        chute = str(input('Digite uma letra: ')).strip().upper()
        print(f'jogando...')

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
            print(f'{letras_acertadas} faltam {letras_acertadas.count("_")} '
                  f'letras')
            if letras_acertadas.count('_') == 0:
                print(f'Parabéns você acertou a palavra é'
                      f' {palavra_secreta.upper()}!')
                acertou = True
        else:
            tentativa += 1
            print(f'OPS!! Você errou! Faltam {6 - tentativa} tentativas.')
            enforcou = tentativa == 6
            if enforcou:
                print('Você excedeu o número de tentativas. Você perdeu!!')

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar()