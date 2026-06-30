from dataclasses import dataclass, field
import json

@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

    def get_discounted_price(self, discount_percent: float) -> float:
        return round(self.price * (1 - discount_percent / 100), 2)

item = Product(name="Wireless Mouse", price=49.99, tags=["electronics", "tech"])
json_data = json.dumps(item.__dict__, indent=2)

print(f"Serialized Product:\n{json_data}")