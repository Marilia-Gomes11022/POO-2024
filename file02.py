notaf = int(input('Digite sua nota final: '))
presenca = float(input('Digite sua presença final: '))
#if notaf >= 60 and presenca >= 75:
#    print('Você está APROVADO')
#else:
#    print('Você está REPROVADO')


if presenca >= 75:
    if notaf >= 6:
        print('O aluno está APROVADO')
    elif 3 < notaf < 6:
        print('O aluno está em RECUPERAÇÃO')
    else:
        print('O aluno está REPROVADO')
else:
    print('Você está REPROVADO')

# + 0,1 na nota!!
    