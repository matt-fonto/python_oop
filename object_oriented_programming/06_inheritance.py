from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    # class attribute
    fleet_count = 0

    def __init__(self, make: str, model: str, year:int):
        # instance attributes
        self._make = make
        self.model = model
        self.year = year
        Vehicle.fleet_count += 1
    
    #Abstract method (forces subclasses to implement)
    @abstractmethod
    def display_info(self):
        """ Abstract method for displaying vehicle info """
        pass

    #Instance method
    def age(self, current_year: int) -> int:
        return current_year - self.year
    
    @classmethod
    def total_vehicles(cls):
        return f"Total vehicles in fleet: {cls.fleet_count}"
    
    @staticmethod
    def is_motorized(vehicle_type: str) -> bool:
        return vehicle_type.lower() in ['car', 'truck', 'motorcycle']

    @property 
    def make(self):
        """ Getter for make """
        return self._make
    
    @make.setter
    def make(self, value):
        """ Setter for make with lenght validation """
        if len(value) < 2:
            raise ValueError("Make name too short")
        self._make = value

    # Magic method (dunder method) for representation
    def __repr__(self) -> str:
        return f"{self.__class__.name}({self.make}, {self.model}, {self.year})"

# Subclass for Motorcycles (Inheritance)
class Motorcycle(Vehicle):
    def __init__(self, make:str, model:str, year: int, has_sidecar:bool):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar # Additional instance attribute for Motorcyle

    def display_info(self):
        sidecar_info = "With sidecar" if self.has_sidecar else "without sidecar" # In Python we use this instead of ternary operator
        # variable = return this if condition true else return that
        # in js: const sidecarInfo = hasSidecar ? "with side car" : "without sidecar"
        return f"Motorcyle: {self.make} {self.model}, Year: {self.year}, {sidecar_info}"

# Subclass for Cars (Inheritance)
class Car(Vehicle):
    def __init__(self, make:str, model:str, year:int, doors:int):
        super().__init__(make, model, year)
        self.doors = doors # Additional instance att for Car
    
    # override abstract method
    def display_info(self):
        return f"Car: {self.make} {self.model}, Year: {self.year}, Doors: {self.doors}"
    
# Subclass for ElectricCars (Polymorphism)
class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, doors:int, battery_capacity: int):
        super().__init__(make, model, year, doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"Electric Car: {self.make} {self.model}, Year: {self.year}, Doors: {self.doors}, Battery: {self.battery_capacity}"

motorcycle = Motorcycle("Harley-Davidson", 'model 2', 2023, False)
car = Car('BMW', "Bmw 5 model rtx", 2022, 4)
electric_car = ElectricCar("Tesla", "Model S", 2022, 4, 90)

print(motorcycle.display_info())
print(car.display_info())
print(electric_car.display_info())