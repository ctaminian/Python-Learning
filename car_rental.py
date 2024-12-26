class CarRental:
    def __init__(self):
        self.fleet = {}
    
    def add_car(self, registration, model, price, available):
        if not isinstance(registration, str) or not registration.strip():
            raise ValueError("Enter a valid registration number.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Enter a valid car model.")
        if not isinstance(price, int) or not price > 0:
            raise ValueError("Enter a valid rent price per day.")
        if not isinstance(available, bool):
            raise ValueError("Enter a valid availability.")
        else:
            self.fleet[registration] = {"model": model, "price_per_day": price, "available": available}

    def remove_car(self, registration):
        if registration not in self.fleet:
            raise ValueError("Car not found in the fleet.")
        if not self.fleet[registration]["available"]:
            del self.fleet[registration]
        else:
            print("Cannot delete this car, it's available for rent.")
    
    def get_available_cars(self, price):
        return list(filter(lambda car: car[1]["price_per_day"] <= price and car[1]["available"], self.fleet.items()))

    def apply_discount(self):
        for car in self.fleet.values():
            car["price_per_day"] *= 0.9

    def get_rented_cars(self):
        return dict(filter(lambda car: not car[1]["available"], self.fleet.items()))

    def __str__(self):
        return f"A fleet of cars available for rent: {self.fleet}"

fleet = CarRental()
fleet.add_car("AXY123", "Tesla Model Y", 150, True)
fleet.add_car("ABC123", "Toyota Corolla", 40, True)
fleet.add_car("XYZ789", "Ford Fiest", 35, False)
fleet.add_car("DEF456", "Honda Civic", 50, True)
fleet.add_car("GHI321", "Tesla Model 3", 100, False)

print(fleet.get_available_cars(50))
fleet.remove_car("XYZ789")
fleet.apply_discount()
print(fleet.get_rented_cars())
print(fleet)