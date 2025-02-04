#12/11/2024
#DICIONÁRIOS

Pessoa = {
        'Nome': 'Tiago',
        'idade': 28, 
        'endereço': {
            'rua': 'Rua Joaquim Teodoro',
            'número': 50,
            'bairro': 'nova parnamirim'
           }
           }
Pessoa['endereço']['bairro'] = 'Alecrim'  # o primeiro [] indica a "primeira camada", e o segundo [] indica a "segunda camada", que neste caso já é o item
Pessoa['idade'] = 30


print(end='--==========--')
print('\n\n', Pessoa, '\n\n')

get_idade = Pessoa.get('idade')

print('A idade é: ', get_idade)

print(end='\n--==========--')


#clear()
#get()