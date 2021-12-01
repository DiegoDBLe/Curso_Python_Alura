import random


def jogar():

    imprime_msg_abertura()
    palavra_secreta = arquivo_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou  = False
    tentativa = 0
    contador  = 0

    print(f'A palavra contém {len(letras_acertadas)} letras: {letras_acertadas}')

    while not enforcou and not acertou:
        contador += 1
        if contador == 9:
            print(f'Encerrando o jogo... Após {contador} tentativas. Você perdeu!!')
            desenho_caveira()
            break
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

            if letras_acertadas.count('_') == 0:
                msg_ganhou(palavra_secreta)
                break
        else:
            tentativa += 1
            if msg_perdeu(tentativa):
                break
    print('Fim do jogo!')


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")


def desenho_caveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def msg_perdeu(tentativa):
    '''
    Função que imprimi mensagem de erro, excedeu o numeros de tentativas para
    acertar a palavra.
    :param tentativa: Contagem de tentativas que o usuario tem para acertar a
     palavra_secreta.
    :return: Variavel de valor booleano que se o usuario não acertar a
    palavra em até 5 tentativas e perde o jogo.
    '''
    print(f'OPS!! Você errou! Faltam {8 - tentativa} tentativas.')
    enforcou = tentativa == 8
    desenha_forca(tentativa)
    if enforcou:
        print('Você excedeu o número de tentativas. Você perdeu!!')
        desenho_caveira()
    return enforcou


def msg_ganhou(palavra_secreta):
    '''
    Função que imprimi mensagem se o jogador acertou a palavra secreta.
    :param palavra_secreta: Recebe a palavra_secreta como parametro
    colocando-a em maiusculo.
    :return: Valor booleano da variavel se o usuario acertou a palavra.
    '''
    print(f'Parabéns você acertou a palavra é {palavra_secreta.upper()}!')
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:       /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    acertou = True
    return acertou


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    '''
    Função que adiciona a letra acertada pelo jogador na posição acertada. O
    For faz a varredura em cada letra da palavra_secreta e se o chute do
    jogador for igual a letra ou seja se o jogador acertou a letra, a mesma é
    adicionada na lista na posição correta.
    :param chute: É a letra que o jogador escolheu(digitou)
    :param palavra_secreta: palavra randomizada na lista que o jogador tem
    que adivinhar.
    :param letras_acertadas: As letras que jogador vai acertando vai sendo
    adicionada na lista e contando quantas letras faltam.
    :return:  sem retorno
    '''
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
    print(f'{letras_acertadas} faltam {letras_acertadas.count("_")} '
          f'letras')


# Função que pede o chute do usuário.
def pede_chute():
    '''
    Função que pede o chute do usuário, tira os espaços e coloca todas as
    letras em maiuscula.
    :return: chute
    '''
    chute = str(input('Digite uma letra: ')).strip().upper()
    print(f'jogando...')
    return chute


def imprime_msg_abertura():
    '''
    Função que imprimi a mensagem de bem vindo!
    :return: sem retorno.
    '''
    print('*' * 33)
    print('   Bem Vindo ao Jogo de Forca!')
    print('*' * 33)


def arquivo_palavra_secreta():
    '''
    - Função que faz abertura de um arquivo txt, tem uma variavel que recebe
    uma lista. Nesse arquivo fica todas as palavras que pode ser randomizadas
    para o jogador tentar acertar.
    - For em cada linha do aqruivo e adiciona na lista palavra[].
    - Fecha o arquivo atraves do método close()
    - Variavel numero recebe a randomização do indice de 0 até o tamanho da
    palavra adicionado na lista.
    - Variavel palavra_secreta recebe o indice(palavra) da lista palavra e
    coloca todas as palavaras em maiuscula.
    :return: pavavra_secreta quem vão tentar adivinha
    '''
    arquivo = open('palavra.txt', 'r')
    palavra = []

    for linha in arquivo:
        palavra.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavra))

    palavra_secreta = palavra[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    '''
    Função que faz um For em cada letra da palavra e vai adicionando os
    espaços ou seja. Se a palavra tem 5 letras ela adiciona 5 _ espaços para
    receber a letra acertada pelo jogador.
    :param palavra: parametro que é uma lista onde está a palavra secreta.
    :return: retorna o For na lista.
    '''
    return ['_' for letra in palavra]  # ou letras_acertadas = list("_" * len(palavra_secreta))


if __name__ == '__main__':
    jogar()