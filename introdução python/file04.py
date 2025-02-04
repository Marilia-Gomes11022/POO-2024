import random 
cond = False
num = 0
while not cond:
    num = random.randint(1,100)
    print(num, end=" ")
    if num % 7 == 0:
        # print(num, end=" ")
        cond = True

