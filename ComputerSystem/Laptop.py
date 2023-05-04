from ComputerSystem.Computer import Computer


class Laptop(Computer):

    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def hibernate(self):
        print("Hibernating...")
