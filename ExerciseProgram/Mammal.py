"""Next, create a derived class Mammal from Animal with an additional attribute fur_color.
Override the make_sound() method in Mammal to print a sound that a mammal makes, such as a roar,
 a bark, or a meow."""
from ExerciseProgram.Animal import Animal


class Mammal(Animal):

    def __init__(self, color):
        self.animal_color = color

    def make_sound(self, animal_type=None):
        self.mammal_Type(animal_type)

    def move(self):
        print("A mammal is moving.")

    def mammal_Type(self, animal_type):
        if animal_type in "Dog":
            print("A {0} a sound bark ".format(animal_type))
        elif animal_type in "Lion":
            print("A {0} makes a sound roar ".format(animal_type))
        elif animal_type in "Cat":
            print("A {0} makes a sound meow ".format(animal_type))
        else:
            print("Animal name in not in list")



