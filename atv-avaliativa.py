from random import randint
mymelody =  1, randint(1,100)
print("Adivinhe que número de 1 a 100 que a My Melody está pensando...")
from random import randint
print("-=-"*20)
print("My Melody vai pensar em um número agora... Tente adivinhar!")
print("-=-"*20)
jogador = int(input("Digite o número que eu estou pensando"))
print("PROCESSANDO...")




if jogador < mymelody:
    print('Ah, que pena! Esta ainda não é a resposta!\n O número digitado é menor do que o Número Secreto ')

if jogador == mymelody:
    print("Uau, como você conseguiu??")
else:
    print("Uau, como você consegue ser tão burro!! O número era {} e não {}".format(mymelody,jogador))

while jogador < mymelody:
    if jogador < mymelody:
        print('Ah, que pena! Esta ainda não é a resposta!\n O número digitado é menor do que o Número Secreto ')


        