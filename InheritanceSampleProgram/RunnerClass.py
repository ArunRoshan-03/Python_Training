from InheritanceSampleProgram.ElectricCar import ElectricCar
from InheritanceSampleProgram.Dog import Dog


class RunnerClass:

    electricCar = ElectricCar(250, 20, "Tesla Model S", 100)
    print(electricCar)
    electricCar.drive(100)

    dog = Dog("Bull", 8, "Bulldogs", "black")
    dog.make_Sound("woof")
