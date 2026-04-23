import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict[str, int]) -> float:
        return sum(self.products[product] * count for product, count in product_cart.items())

    def print_receipt(self, customer_name: str, product_cart: dict[str, int]) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0.0
        for product, count in product_cart.items():
            price = self.products[product]
            cost = count * price
            total_cost += cost

            display_cost = int(cost) if cost == int(cost) else cost
            print(f"{count} {product}s for {display_cost} dollars")

        display_total = int(total_cost) if total_cost == int(total_cost) else total_cost
        print(f"Total cost is {display_total} dollars")
        print("See you again!")
