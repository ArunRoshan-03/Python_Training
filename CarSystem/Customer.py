class Customer:
    def __init__(self, name, driver_license_number):
        self.name = name
        self.driver_license_number = driver_license_number
        self.rental_history = []

    def add_rental(self, rental):
        self.rental_history.append(rental)
