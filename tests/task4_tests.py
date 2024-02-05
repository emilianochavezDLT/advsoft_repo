from main import Product, Service

def test_product_discount():
    product = Product()
    assert product.calculate_discount(50, 0.10) == 45, "should be 70"

def test_service_discount():
    service = Service()
    assert service.calculate_discount(235, 0.40) == 141, "should be 180"

def test_product_discount_2():
    product = Product()
    assert product.calculate_discount(0, 0.30) == 0, "should be 70"

def test_service_discount_2():
    service = Service()
    assert service.calculate_discount(0, 0.10) == 0, "should be 180"