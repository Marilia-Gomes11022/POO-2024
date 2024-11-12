# 12/11/2024

alunos = ['Marília', 'Pedro', 'Yasmin']

alunos.insert(0, 'Marcos')
alunos.insert(0, 'João Vitor')

print('\nLista inicial:', alunos, end='\n   ~~~~~~~~~~~~~~~~~~~~~\n')


#resultado = João, Marcos, marília, Pedro, Yasmin
#alunos.remove('João Vitor')  #remove 1 item, mas tem que colocar extamente como está na lista

#print(alunos)

#alunos.pop(3) #remove 1 item, mas tem que colocar a posição(começando pelo 0)


# o remove joga a informação no buraco negro, enquanto no pop a informação ainda fica guardada na numvem/lixeira

alunos_tchau = alunos.pop(0), alunos.pop(3)

print('Alunos com matrícula ativa:', alunos, end='\n   ~~~~~~~~~~~~~~~~~~~~~\n')

print('Alunos que disseram tchau:', alunos_tchau, end='\n   ~~~~~~~~~~~~~~~~~~~~~ \n')
alunos.reverse()
print('A ordem inversa é: ', alunos, end='\n________________________________________________________')



#também podemos usar listas com laços de repetição, como while e for