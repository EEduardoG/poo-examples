
#Importamos ABC y abstractmethod para poder definir clases abstractas.
from abc import ABC, abstractmethod


'''
Autor: Erick García
Fecha 31 de octubre de 2021
Descripción: Con este script, se pretende mostrar
la manera en la que funciona la abstracción en la programación
orientada a objetos, poniendo como ejemplo diferentes animales.
'''

'''
Clase abstracta principal. En esta tenemos los atributos
y metodos que comparten todos nuestros animales.
'''
class Animal(ABC):
    
    __nombre = None
    __sonido = None

    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def emitirSonido(self):
        pass
    
    @abstractmethod
    def comer():
        pass

'''
En esta clase se encuentran los metodos y atributos que deben tener
todos los animales que puedan caminar.
'''
class AnimalCaminante(Animal):
    @abstractmethod
    def caminar():
        pass

'''
En esta clase se encuentran los metodos y atributos que deben tener
todos los animales que puedan nadar.
'''
class AnimalNadador(Animal):
    @abstractmethod
    def nadar():
        pass

'''
En esta clase se encuentran los metodos y atributos que deben tener
todos los animales que puedan volar.
'''
class AnimalVolador(Animal):
    @abstractmethod
    def volar():
        pass

'''
Esta clase no hereda de Animal debido a que no se acompla 
a nuestro diseño. Sin embargo no prestemos atención a esto.
'''
class AnimalConPatas(ABC):
    __patas = 0
    

'''
La clase que nos permitirá construir a nuestro perro.
'''
class Perro(AnimalCaminante,AnimalNadador,AnimalConPatas):

    #Asignamos valor a los atributos.
    Animal.__nombre = 'Perro'
    AnimalConPatas.__patas = 4
    Animal.__sonido = 'Guau guau'

    '''
    Estos métodos están siendo sobrescritos de la clase Animal.
    Si borramos estos metodos nos dará un error que básicamente
    nos dice que nos falta implementarlos..
    '''
    def presentarse(self):
        print("Hola. Soy un " + self.__nombre)

    def emitirSonido(self):
        print(self.__sonido)

    def comer(self):
        print(self.__nombre + ': ¡Yumi! Estoy comiendo :D')

    '''
    Estos métodos están siendo sobrescritos de la clase AnimalCaminante.
    Si borramos estos metodos nos dará un error que básicamente
    nos dice que nos falta implementarlos..
    '''

    def caminar(self):
        print(self.__nombre + ': Estoy caminando.')

    '''
    Estos métodos están siendo sobrescritos de la clase AnimalNadador.
    Si borramos estos metodos nos dará un error que básicamente
    nos dice que nos falta implementarlos..
    '''
    def nadar(self):
        print(self.__nombre + ': Estoy nadando.')


'''
La clase que nos permitirá construir a nuestro gato.
'''
class Gato(AnimalConPatas,AnimalCaminante):

    Animal.__nombre = 'Gato'
    AnimalConPatas.__patas = 4
    Animal.__sonido = 'Miau Miau'

    def presentarse(self):
        print("Hola. Soy un " + self.__nombre)

    def emitirSonido(self):
        print(self.__sonido)

    def comer(self):
        print(self.__nombre + ': ¡Yumi! Estoy comiendo :D')

    def caminar(self):
        print(self.__nombre + ': Estoy caminando.')

'''
La clase que nos permitirá construir a nuestro pato.
'''
class Pato(AnimalConPatas,AnimalCaminante,AnimalNadador,AnimalVolador):

    Animal.__nombre = 'Pato'
    AnimalConPatas.__patas = 2
    Animal.__sonido = 'Cuack Cuack'

    def presentarse(self):
        print("Hola. Soy un " + self.__nombre)

    def emitirSonido(self):
        print(self.__sonido)

    def comer(self):
        print(self.__nombre + ': ¡Yumi! Estoy comiendo :D')

    def caminar(self):
        print(self.__nombre + ': Estoy caminando.')

    def volar(self):
        print(self.__nombre + ': Estoy volando.')

    def nadar(self):
        print(self.__nombre + ': Estoy nadando.')

'''
La clase que nos permitirá construir a nuestro delfín.
'''
class Delfin(AnimalNadador):

    Animal.__nombre = 'Delfin'
    Animal.__sonido = 'ihiertgiedjirgijgij'

    def presentarse(self):
        print("Hola. Soy un " + self.__nombre)

    def emitirSonido(self):
        print(self.__sonido)

    def comer(self):
        print(self.__nombre + ': ¡Yumi! Estoy comiendo :D')

    def nadar(self):
        print(self.__nombre + ': Estoy nadando.')


#Instanciamos a nuestro animal
animal = Perro()

#Porvemos diferentes métodos de nuestro animal...
animal.emitirSonido()




