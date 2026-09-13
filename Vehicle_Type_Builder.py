# 1. Create a parent vehicle class
class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Max Speed: {self.speed} km/h")
        print(f"Mileage: {self.mileage} km/l")

    # This method will be overridden by the child class
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."


# 2. Build a child car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, name, speed, mileage, brand):
        # 5. Use super() to inherit parent features/attributes
        super().__init__(name, speed, mileage)
        self.brand = brand # Specific attribute for Car

    # 4. Override a method from the parent class
    def seating_capacity(self, capacity=5):
        # We can use super() here too, or entirely change the behavior
        default_message = super().seating_capacity(capacity)
        return f"{default_message} (Standard for {self.brand} cars)"


# --- Main Execution / Testing ---
if __name__ == "__main__":
    print("--- Creating a Parent Vehicle Object ---")
    my_vehicle = Vehicle("School Bus", 80, 10)
    my_vehicle.display_info()
    print(my_vehicle.seating_capacity(50))
    
    print("\n--- Creating a Child Car Object ---")
    my_car = Car("Model S", 250, 15, "Tesla")
    my_car.display_info() # Inherited from Vehicle
    print(my_car.seating_capacity()) # Overridden method in action
    
    print("\n--- Checking Inheritance Relationship ---")
    # 6. Check the inheritance relationship with issubclass()
    is_child = issubclass(Car, Vehicle)
    print(f"Is 'Car' a subclass of 'Vehicle'?: {is_child}")