"""Create two more derived classes from Mammal: Cat class should have an additional attribute eye_color."""
from ExerciseProgram.Mammal import Mammal


class Cat(Mammal):

    """ This a Constructor  method to initialised animal eye_colour """
    def __init__(self, color, eye_color):
        super().__init__(color)
        self.animal_EyeColor = eye_color

    """ This method is override from Animal class"""
    def make_sound(self, animal_type=None):
        super().mammal_Type(animal_type)

    """ This method is override from Animal class"""
    def move(self):
        print("A cat is walking.")

    """ This method is used called the Cat EyeColor"""
    def __str__(self):
        return f"This cat has {self.animal_EyeColor} eyes."
