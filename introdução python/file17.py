#DESAFIO

#criar uma função para validar se a pessoa pode ou não entrar no evento
#Se homem maior igual que 18 anos >>PODE<< entrar e o nome não pode começar com A,B e C
#Se mulher maior igual que 17 anos >>PODE<< entrar e o nome não pode começar com L, M e N


#tentativa 1
def validar(genero, idade, letra1):
    genero = input('Digite o gênero(H ou M): ')
    idade = int(input('Digite a idade: '))
    letra1 = input('Digite a primeira letra: ')

    if genero == "homem":
        if idade >= 18:
            resultado = "ACESSO PERMITIDO"
            if letra1 != "A" "B" "C":
                resultado = "ACESSO PERMITIDO"
            else: 
                resultado = "ACESSO NEGADO"
        else:
            resultado = "ACESSO NEGADO"

        return resultado
        


print(resultado)



def validar(genero, idade, letra1):
    resultado = "NÃO IDENTIFICADO"
    if genero == "H" and idade >= 18 and letra1 != "A" "B" "C":
        resultado = "Acesso permitido"
    else: 
        resultado = "Acesso negado"
print(resultado)