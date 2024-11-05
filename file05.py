#utilizando o for
# For (sabe a quantidade de repetições)
# While (não sabe a quantidade exata de repetições), pode ser infinito


lista_de_alunos = ['Kevem', "Pedro", 'Joana', 'Márcia', 'Marília']
aluno1 = 'Márcia'
aluno2 = 'Jonathan'

#for i in [0,1,'Joana',3,4,5,'10',20]: #pode ser chamdo de Lista, vetor, array
for alunos in lista_de_alunos:
    if aluno1 in lista_de_alunos:
        print(aluno1, 'está na lista')
    if aluno2 in lista_de_alunos:
        print(aluno2, 'está na lista')
    else:
        print(aluno2, 'não está na lista')
    break



