class HTMLGenerator:
    def __init__(self):
        self.stock = dict()

    def add_product(self, product, quantity):
        # function to add a product to the stock
        if product not in self.stock:
            self.stock[product] = 0
        self.stock[product] += quantity

    def generate_table(self):
        table_string = "<table><tr><th>Product</th><th>Quantity</th></tr>"
        for product in self.stock:
            table_string += f"<tr><td>{product}</td><td>{self.stock[product]}</td></tr>"
        table_string += "</table>"
        return table_string
