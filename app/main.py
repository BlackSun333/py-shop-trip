import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**c) for c in config["customers"]]
    shops = [Shop(**s) for s in config["shops"]]

    for i, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        min_total_cost = float("inf")

        for shop in shops:
            trip_fuel_cost = customer.calculate_trip_cost(shop.location, fuel_price)
            products_cost = shop.calculate_products_cost(customer.product_cart)
            total_cost = trip_fuel_cost + products_cost
            print(f"{customer.name}'s trip to the {shop.name} costs {round(total_cost, 2)}")
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                cheapest_shop = shop

        if cheapest_shop and customer.money >= min_total_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            print(f"\n{customer.name} rides home")
            customer.money -= min_total_cost
            customer.location = cheapest_shop.location

            display_money = int(customer.money) if customer.money == int(customer.money) else round(customer.money, 2)
            print(f"{customer.name} now has {display_money} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")

        if i < len(customers) - 1:
            print()
