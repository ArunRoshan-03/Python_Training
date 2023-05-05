class Rental:
    def __init__(self, car, customer, start_date, end_date):
        self.car = car
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date

    def get_rental_duration(self):
        return (self.end_date - self.start_date).days

    def get_rental_cost(self):
        duration = self.get_rental_duration()
        return duration * self.car.rental_price

    def return_car(self):
        self.customer.add_rental(self)
