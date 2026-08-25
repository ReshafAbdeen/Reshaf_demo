import pytest

# Target Functions to Test
def calculate_discount(price: float, discount_pct: float) -> float:
    if price < 0 or not (0 <= discount_pct <= 100):
        raise ValueError("Invalid price or discount percentage")
    return round(price * (1 - discount_pct / 100), 2)

# 1. Test Fixture Setup
@pytest.fixture
def sample_product():
    return {"name": "Laptop", "price": 50000.0}

# 2. Basic Test Case
def test_valid_discount(sample_product):
    final_price = calculate_discount(sample_product["price"], 10)
    assert final_price == 45000.0

# 3. Parameterized Testing (Multiple Edge Cases)
@pytest.mark.parametrize("price, discount, expected", [
    (100.0, 0, 100.0),
    (200.0, 50, 100.0),
    (99.99, 10, 89.99),
])
def test_discount_variations(price, discount, expected):
    assert calculate_discount(price, discount) == expected

# 4. Exception Testing
def test_invalid_discount_raises_error():
    with pytest.raises(ValueError):
        calculate_discount(100.0, 150)  # Invalid discount > 100%