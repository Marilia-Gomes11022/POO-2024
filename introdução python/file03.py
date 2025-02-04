#Estruturas de repetição
# For (sabe a quantidade de repetições)
# While (não sabe a quantidade exata de repetições), pode ser infinito

mult = 75 % 4
print(mult)

i = 0

while i < 10:
    print(i)
    i = i + 1
#estando dentro da identação, vai somar toda vez que rodar, enquanto se fora, vai permanecer o valor
    

#imprimir os dez primeiros múltiplos de 75
#imprimir números aleatórios até aparecer um múltiplo de 7
i = 1
while i<= 10:
    print(i * 75, end=" ")
    i += 1

import random 

x = random.randint(1,100)
while x != (x * 7):
    if True:
        print(x)
print(x)



#counter = 0
#cond = False#

#while not cond





while not cond:
    num = random.randint(1,100)
    if num % 7 == 0:
        print(num, end=" ")
        cond = True
