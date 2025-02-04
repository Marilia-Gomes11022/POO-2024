#12/11/2024
#TUPLAS
tupla = (1, 2, 3, 5, 'Tiago', 10.5, ['número 1', 'número 2'])

#você pode adicionar uma lista DENTRO de um tupla
#uma tupla PODE ser concatenada


print('\n\n\n\nANTES:', tupla, end='\n --==========--\n')

tupla[6][0] = 'valor alterado' 
# o primeiro índice(nesse caso [6]), indica o item da TUPLA, enquanto o [0], indica o item de dentro da lista

print('DEPOIS:', tupla, '\n\n\n\n')

tupla = tupla + ('outro valor', 'outro valor 2')

