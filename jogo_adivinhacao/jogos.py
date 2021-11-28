import adivinhacao
import forca

print('*' * 33)
print('      Escolha seu jogo!')
print('*' * 33)
print()

print('- Digite (1) Para o jogo da Froca.\n- Digite (2) Para o jogo de '
      'Adivinhação.')
print()
jogo = int(input('Qual jogo você deseja jogar ? :'))

if jogo == 1:
    print('Jogo da Forca selecionado!')
    forca.jogar()
elif jogo == 2:
    print('Jogo de Adivinhação selecionado!')
    adivinhacao.jogar()
