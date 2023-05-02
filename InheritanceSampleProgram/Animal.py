class Animal:

    def __init__(self, name, age):
        self.animal_Name = name
        self.animal_Age = age

    def make_Sound(self, animal_Sound):
        print(f"{self.animal_Name} makes a {animal_Sound} sound.")
