class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        if product.purchase(quantity):
            self.items.append((product, quantity))
            print(f"Added {quantity}x {product.name} to cart.")

    def calculate_total(self, tax_rate: float = 0.08) -> float:
        subtotal = sum(prod.price * qty for prod, qty in self.items)
        total = subtotal * (1 + tax_rate)
        return round(total, 2)

# --- Using the new classes ---
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(ebook, 1)
print(f"Total Cart Price (with tax): ${cart.calculate_total()}")