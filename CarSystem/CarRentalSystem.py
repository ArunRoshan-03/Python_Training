from datetime import date, timedelta

from CarSystem.Rental import Rental


class CarRentalSystem:
    def __init__(self):
        self.available_cars = []
        self.rented_cars = []

    def add_car(self, car):
        self.available_cars.append(car)
        print(f"Added car {car.make} {car.model} ({car.year}) to available cars.")

    def rent_car(self, customer, car, start_date, end_date):
        if car not in self.available_cars:
            print("This car is not available for rent.")
            return None

        rental = Rental(car, customer, start_date, end_date)
        self.rented_cars.append(rental)
        self.available_cars.remove(car)

        customer.add_rental(rental)
        car.add_rental(rental)

        print(f"Rented car {car.make} {car.model} ({car.year}) to {customer.name} ({customer.driver_license}).")

        return rental

    def return_car(self, rental):
        if rental not in self.rented_cars:
            print("This rental does not exist.")
            return None

        rental.car.remove_rental(rental)
        rental.customer.remove_rental(rental)
        self.rented_cars.remove(rental)
        self.available_cars.append(rental.car)

        print(f"Returned car {rental.car.make} {rental.car.model} ({rental.car.year}).")

        return rental

    def display_available_cars(self):
        if not self.available_cars:
            print("No cars available for rent.")
            return

        print("Available cars:")
        for car in self.available_cars:
            print(f"{car.make} {car.model} ({car.year}), ${car.price_per_day}/day")

    def display_customer_rental_history(self, customer):
        print(f"Rental history for {customer.name}:")
        for rental in customer.rental_history:
            print(
                f"- {rental.car.make} {rental.car.model} ({rental.car.year}), rented from {rental.start_date} to {rental.end_date}")