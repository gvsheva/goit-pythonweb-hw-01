from abc import ABC, abstractmethod
import logging


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    def __str__(self):
        return f"{self.make} {self.model} ({self.spec} Spec)"

    @abstractmethod
    def start_engine(self):
        raise NotImplementedError


class Car(Vehicle):
    def start_engine(self):
        logging.info("%s: Двигун запущено", self)


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info("%s: Мотор заведено", self)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")
