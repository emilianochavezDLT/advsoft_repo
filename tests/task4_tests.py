from main import Product, Service

def test_product_discount():
    product = Product()
    assert product.calculate_discount(50, 0.10) == 45, "should be 70"

def test_service_discount():
    service = Service()
    assert service.calculate_discount(200, 0.10) == 180, "should be 180"