from InheritanceSampleProgram.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, max_Speed, mileage, brand):
        super().__init__(max_Speed, mileage)
        self.car_brand = brand

    def __str__(self):
        return f"Car Band is {self.car_brand}, its give mileage {self.mileage} km/h"

    def drive(self, speed):
        print(f"Driving a {self.car_brand} at {speed} km/h")
