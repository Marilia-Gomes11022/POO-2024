from random import randint
mymelody = randint(1, 100)
print('Sou seu computador... Acabei de pensar em um número entre 1 e 100.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
max = 7

while not acertou and palpites < max:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == mymelody:
        acertou = True
    elif jogador < mymelody and palpites < max:
        print('Mais... Tente mais uma vez.')
    elif jogador > mymelody:
        print('Menos... Tente mais uma vez.')
    elif jogador != mymelody:
        print('')

if acertou:
    print('Acertou com {} tentativas. Parabéns!'.format(palpites))
else:
  print('Suas tentativas acabaram!\nO número era {}'.format(mymelody))

