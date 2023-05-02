from InheritanceSampleProgram.Car import Car


class ElectricCar(Car):

    def __init__(self, max_Speed, mileage, brand, battery_level):
        super().__init__(max_Speed, mileage, brand)
        self.battery_capacity = battery_level

    def drive(self, speed):
        print(f"Driving an electric {self.car_brand} at {speed} km/h")
        range_speed = self.battery_capacity * 5 * (self.max_Speed - speed)
        print(f"Range of the car: {range_speed} km")