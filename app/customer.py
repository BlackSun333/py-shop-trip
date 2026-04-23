import math
from app.car import Car

class Customer:
    def __init__(self, name: str, product_cart: dict[str, int], location: list[int], money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_trip_cost(self, shop_location: list[int], fuel_price: float) -> float:
        distance = math.sqrt(
            (self.location[0] - shop_location[0]) ** 2 +
            (self.location[1] - shop_location[1]) ** 2
        )
        fuel_needed = (distance * 2 / 100) * self.car.fuel_consumption
        return fuel_needed * fuel_price
