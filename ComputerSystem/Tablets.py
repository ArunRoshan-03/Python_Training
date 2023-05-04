from ComputerSystem.Computer import Computer


class Tablets(Computer):

    def __init__(self, brand, model, price, screen_size):
        super().__init__(brand, model, price)
        self.screen_size = screen_size

    def take_photo(self):
        print("Taking a photo...")
