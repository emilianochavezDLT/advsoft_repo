from main import Product, Service

# To test on pytest, In replit I used the command:
# pytest tests/task4_tests.py

def test_product_discount():
    product = Product()
    assert product.calculate_discount(50, 0.10) == 45, "should be 70"

def test_service_discount():
    service = Service()
    assert service.calculate_discount(235, 0.40) == 141, "should be 180"

def test_product_discount_2():
    product = Product()
    assert product.calculate_discount(0, 0.30) == 0, "should be 0"

def test_service_discount_2():
    service = Service()
    assert service.calculate_discount(0, 0.10) == 0, "should be 0"

