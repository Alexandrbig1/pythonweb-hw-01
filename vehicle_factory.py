from abc import ABC, abstractmethod

# Step 1: Create an abstract base class Vehicle
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

# Step 2: Modify Car and Motorcycle to inherit from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")

# Step 3: Create an abstract class VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Step 4: Implement USVehicleFactory and EUVehicleFactory
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} {model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} {model} (US Spec)")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} {model} (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} {model} (EU Spec)")

# Usage
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()