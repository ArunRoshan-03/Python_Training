from ExerciseProgram.Cat import Cat
from ExerciseProgram.Dog import Dog


class RunnerClass:
    dog = Dog("Black", "Golden Retriever")
    print(dog)
    dog.make_sound("Dog")
    dog.move()

    cat = Cat("Black", "Brown")
    print(cat)
    cat.make_sound("Cat")
    cat.move()
