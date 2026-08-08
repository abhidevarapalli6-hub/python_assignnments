class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=18):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 65)
        print("                         BILL")
        print("=" * 65)

        print(
            f'{"Product":<25}'
            f'{"Price":>10}'
            f'{"Qty":>8}'
            f'{"Amount":>12}'
        )

        print("-" * 65)

        for product in self.products:
            print(
                f"{product.name:<25}"
                f"₹{product.price:>8.2f}"
                f"{product.quantity:>8}"
                f"₹{product.get_total():>10.2f}"
            )

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print("-" * 65)
        print(f'{"Subtotal":>53} ₹{subtotal:>10.2f}')
        print(f'{"Tax (18%)":>53} ₹{tax:>10.2f}')
        print(f'{"Final Total":>53} ₹{total:>10.2f}')
        print("=" * 65)


# Example
bill = Bill()

bill.add_product(Product("Laptop Bag", 1200, 1))
bill.add_product(Product("Wireless Mouse", 600, 2))
bill.add_product(Product("Keyboard", 900, 1))

bill.display_bill()
