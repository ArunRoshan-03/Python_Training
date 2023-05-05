from CarSystem.Car import Car
from CarSystem.CarRentalSystem import CarRentalSystem
from CarSystem.Customer import Customer


class RunnerClass:
    car1 = Car("Toyota", "Corolla", 2020, 50)
    car2 = Car("Honda", "Civic", 2019, 45)
    car3 = Car("Ford", "Fiesta", 2018, 40)

    # Create some customers
    customer1 = Customer("John Doe", "DL1234")
    customer2 = Customer("Jane Smith", "DL5678")

    # Create the car rental system
    system = CarRentalSystem()

    # Add the cars to the system
    system.add_car(car1)
    system.add_car(car2)
    system.add_car(car3)

    # Display the available cars
    system.display_available_cars()

    # Rent a car to a customer
    rental1 = system.rent_car(car1, customer1, "2023-06-01", "2023-06-05")
    print(rental1)

    # Display the available cars again
    system.display_available_cars()

    # Return the rented car
    system.return_car(rental1)

    # Display the available cars once more
    system.display_available_cars()

    # Display the rental history of a customer
    system.display_customer_rental_history(customer1)

