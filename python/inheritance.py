'''
Author: Erick García
Date: November 03 2021
Description: With this script, it is intended to show
the way inheritance works in programming
object-oriented, taking as an example the realization of
a cake.
'''

#import abc library and abstactmethod to allow us create abstract classes.
from abc import ABC, abstractmethod


#Define a ingredient.
class Ingredient:
    #Constructor of ingredient
    def __init__(self, name,measure):
        #Name of ingredient
        self.name = name 
        #unit of measurement
        self.measure = measure


'''
Class to define quantity of ingredient.
As you can see. This class inherits from the Ingredient class.
So Ingredient is the parent class and IngredientQuantity is his 
child.
'''

class IngredientQuantity(Ingredient):
    def __init__(self,name,measure,quantity):
        '''
        Here we are having access to methods and attributes from
        the parent class. Now we can set attribute values and access to
        methods.
        '''
        super().__init__(name,measure)
        #Define quantity of ingredient.
        self.quantity = quantity

            
#Define a list of ingredients.
class IngredientsList: 
    def __init__(self):
        #Empty list that will be populated with ingredients.
        self.listOfIngredients = []

    #Add a new ingredient to list.
    def addIngredient(self,ingredient):
        print('adding ' + str(ingredient.quantity) + ' ' + ingredient.measure + ' of ' + ingredient.name + '...')
        self.listOfIngredients.append(ingredient)
   

#Abstract class to define food.
class Food(IngredientsList,ABC):

    def __init__(self):
        '''
        It is equal to super(). but because we have multiple inheritance.
        It´s more easy to access in this way.
        '''
        IngredientsList.__init__(self)
        '''
        We will define the name of our food in the setName() method. 
        So we initialize the name empty.'''
        self.name = None

    #Set name of our food.
    def setName(self,str):
        self.name = str
    
    '''
    This is an abstract method. Because all 
    food must be prepared. However, each one has a 
    different way of preparing. So. In this class 
    we declare the method and in his child classes 
    we implement it.
    '''
    @abstractmethod
    def prepare(self):
        pass
    
    #show our instance
    def serve(self):
        print(self)
    

#Abstract class to define Baked food.
class BakedFood(Food):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def bake(self):
        pass

#Define cake.
class Cake(BakedFood):

    def __init__(self):
        super().__init__()

    def prepare(self):
        #TODO: what is the way to preapre a cake?
        print('preparing a delicious cake...')
    
    def bake(self):
        #TODO: what is the way to bake a cake?
        print('baking amazing cake. wait a few minutes...')
        print('Your cake is ready... Enjoy!')
    
    

#create a new cake
cake = Cake()
#Name of our cake.
cake.setName('Pastel de fresas')
#Add ingredients to our cake.
cake.addIngredient(IngredientQuantity('flour','grams', 800 ))
cake.addIngredient(IngredientQuantity('egg','pieces', 2 ))
cake.addIngredient(IngredientQuantity('strawberry','pieces', 10 ))
cake.addIngredient(IngredientQuantity('milk','mililiters', 200 ))
cake.addIngredient(IngredientQuantity('sugar','grams', 20 ))
cake.addIngredient(IngredientQuantity('butter','grams', 10 ))
cake.addIngredient(IngredientQuantity('salt','grams', 2 ))
cake.addIngredient(IngredientQuantity('baking powder','grams', 20 ))
#prepare our cake.
cake.prepare()
#bake the cake.
cake.bake()
#We have now a cake. Enjoy.
cake.serve()

'''
EXAMPLE OF CODE REUSE
We want now a french fries.
The only thing we have to do is declare an abstract FriedFood
class that inherits from Food. Then create FrenchFries class
inherits from FriedFood and we will have access to 
all methods and attributes that help us to define our french fries.
'''

#Abstract class to define fried food.
class FriedFood(Food):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def fry(self):
        pass

#Define french fries.
class FrenchFries(FriedFood):
    def __init__(self):
        super().__init__()

    def prepare(self):
        #TODO: what is the way to preapre a cake?
        print('preparing french fries yumi yumi!...')
    
    def fry(self):
        #TODO: what is the way to bake a cake?
        print('frying our french fries...')
        print('Your french fries are ready... Enjoy!')

'''
With a good abstraction model and using inheritance
We will be able to write code more quickly and efficiently.
'''
fries = FrenchFries()
fries.addIngredient(IngredientQuantity('salt','grams', 10 ))
fries.addIngredient(IngredientQuantity('potatoe','piece', 1 ))
fries.prepare()
fries.fry()
fries.serve()