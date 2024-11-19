# Funções

def minhafuncsoma(numero1, numero2):
    soma = numero1 + numero2
    print(soma)
    return soma
#quando uma função não tem retorno, ela EXECUTA, mas não entrega nada
# se vc precisa receber uma informação e utilizá-la de alguma forma, você PRECISA usar RETURN

valor_soma = minhafuncsoma(10, 20)
print(valor_soma)

#NOME E SOBRENOME

#RETORNAR NOME COMPLETO

def nomeado(nome, sobrenome):
    nome_completo = nome + sobrenome
    return nome_completo

renilda = nomeado("Maria ", "Lucia Renilda")
print('O nome completo é:', renilda)

