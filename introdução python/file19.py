#Recursividade

def fatorial(numero):
    if numero ==1:
        return 1
    return numero*fatorial(numero-1)

print(fatorial(5))

#série de fibonatti

def fib(numero):
    if numero ==1 or numero == 2:
        return 1
    else: 
        return fib(numero-1) + fib(numero-2)
    
    