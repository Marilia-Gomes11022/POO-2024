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


