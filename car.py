class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


def create_car(make, model, year):
    car_instance = Car(make, model, year)
    return car_instance


def main():
    # Prompt user for car details
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")

    # Create car object using user input
    car = create_car(make, model, year)

    # Access attributes and call methods of the car object
    print(f"\nYour car details:")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Year: {car.year}")
    car.read_odometer()


if __name__ == "__main__":
    main()
