"""Create an abstract class Animal with two abstract methods: make_sound() and move().
The make_sound() method should print a generic sound that the animal makes, and the move()
method should print a generic movement that the animal makes (e.g., walk, run, swim, fly, etc.).
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """ This method is used animal make_sound """
    @abstractmethod
    def make_sound(self):
        pass

    """ This method is used animal move """
    @abstractmethod
    def move(self):
        pass
