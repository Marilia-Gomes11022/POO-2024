class Animal:
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def __str__(self):
        return 'Nome: %s \nPeso: %f'%(self.__nome, self.__peso)
    def alimentar(self, comida):
        self.peso += comida
        def __gt__(self, other):
            return self.peso > other.__peso
    def __add__(self, other):
        return Animal(self.__nome + '' + other.__nome, self.__peso + other.__peso)

    @property
    def nome(self):
        print('Getter foi chamdo')
        return self.nome
    @nome.setter
    def nome(self, new_name):
        print('Setter foi chamado')
        if type(new_name) == type(str()):
            self.__nome == new_name
        else:
            print('O nome deve ser uma string')

Leao = Animal('Leao ', 200)
Tigre = Animal('Tigre', 150)
animais = Leao + Tigre
print(animais)

#sobrecarga de operadores

class Mamifero(Animal):
    classe = 'Mamalia'

    def __str__(self):
        return super().__str__() + '\nMamífero\n'

class Ave(Animal):
    def __str__(self):
        return super().__str__() + '\nAve\n'
class Ave_Pequena(Ave):
    pass

Leao = Mamifero('Leao', 200)
print(Leao)


