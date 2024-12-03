# ENCAPSULAMENTO 
# modos: público, privado e protegido

# getters e setters -> funcionam para ver e editar os dados

#diferença entre protegido e privado:

#crie uma classe 

class Pessoa:
    def __init__(self, nome, idade, sala):
        self.nome = nome
        self.__idade = idade
        self.__sala = sala

    def getIdade(self):
        return self.__idade
    def setIdade(self):
        return self.__idade
    
    def getSala(self):
        return self.__sala
    def setSala(self):
        return self.__sala
    

    def gritar(self, fala):
        self.fala = fala.upper()
        return fala.upper()
    
    def andar(self, passos):
        self.passos = passos
        return passos

    def sono(self, horas):
        self.horas = horas
        return horas

aluno1 = Pessoa('marília', 55, 'B078')
aluno1.andar(6)



class Cachorro:
    def __init__(self, nome, idade, raca):
        self.__nome = nome
        self.__idade = idade 
        self.raca = raca

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self):
        return self.__nome
    
    


        return print('O cachorro está comendo')
    
cachorro1 = Cachorro('max', 5, 'vira-lata')
cachorro1.andar()
cachorro1.comer()

cachorro2 = Cachorro('Luci', 4, 'poodle')

