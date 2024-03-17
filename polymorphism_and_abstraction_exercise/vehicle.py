from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle, ABC):
    AIR_CONDITIONER_ON: float = 0.9

    def drive(self, distance: float):
        total_km_fuel = (self.AIR_CONDITIONER_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= total_km_fuel:
            self.fuel_quantity -= total_km_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    AIR_CONDITIONER_ON: float = 1.6
    TANK_PERCENTAGE_FILL: float = 0.95

    def drive(self, distance: float):
        total_km_fuel = (self.AIR_CONDITIONER_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= total_km_fuel:
            self.fuel_quantity -= total_km_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL




