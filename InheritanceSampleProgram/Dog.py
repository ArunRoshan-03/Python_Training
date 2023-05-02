from InheritanceSampleProgram.Animal import Animal


class Dog(Animal):

    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self.animal_breed = breed
        self.animal_color = color

    def make_Sound(self, sound):
        return super().make_Sound(sound), self.__animal_weight(43)

    def __animal_weight(self, weight):
        print(f"Animal weight is {weight}")
