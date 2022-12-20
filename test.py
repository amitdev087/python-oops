# We have entities Animal and Cage.
# We have two more types of entites Dog and Cat and they're Animals.
# Cat makes sound "meow", and dog makes sound "bark".
# We can put the animal in cage.
# We can shake the cage.
# When we shake the cage, the animal in that cage make sound.
# We should be able to get the cound of all the animals

from abc import ABC

class Animal(ABC):
    def sound(self):
        pass


class Cage:
    def __init__(self,animal):
        self.animal=animal

    def shake(self):
        print(self)
        self.sound()
    
        
class Dog(Animal ,Cage):
    def __init__(self):
        super().__init__("Dog")
    
    def sound(self):
        print("bark")


class Cat(Animal,Cage):
    def __init__(self):
        super().__init__("Cat")
    
    def sound(self):
        print("meow")


d=Dog()
d.shake()
c=Cat()
c.shake()