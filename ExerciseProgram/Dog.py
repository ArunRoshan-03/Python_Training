"""Create two more derived classes from Mammal:The Dog class should have an additional attribute
breed."""

"""Override the move() method in both Dog to print the movement that each animal makes 
(e.g., walk, run, etc.). Also, override the str() method in both Dog to print a string 
that includes the breed and the color, respectively."""
from ExerciseProgram.Mammal import Mammal


class Dog(Mammal):
    """ This a Constructor  method to initialised animal bread """
    def __init__(self, color, breed):
        super().__init__(color)
        self.animal_Breed = breed

    """ This method used to find the animal sound, extend from the Animal class """
    def make_sound(self, animal_type=None):
        Mammal.mammal_Type(animal_type)

    """ This method used to displayed the animal Move, extend from the Animal class """
    def move(self):
        print(f"A {self.animal_Breed} is running")

    """ This method is used called the Cat animal_breed and animal_color"""
    def __str__(self):
        return f"This dog is a {self.animal_Breed} with {self.animal_color} fur."
