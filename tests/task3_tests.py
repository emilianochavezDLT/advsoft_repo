from main import sign_check, first_ten_prime_numbers, hundred_number_sum

def test_is_positive():
    is_positive = sign_check(11)
    assert is_positive == "Positive", "should be Positive"

def test_is_negative():
    is_negative = sign_check(-11)
    assert is_negative == "Negative", "should be Negative"

def test_is_zero():
    is_zero = sign_check(0)
    assert is_zero == "Zero", "should be Zero"

def test_first_ten_prime_numbers():
    first_ten = first_ten_prime_numbers()
    assert first_ten == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "should be the first ten prime numbers"

def test_hundred_number_sum():
    hundred_sum = hundred_number_sum()
    assert hundred_sum == 5050, "should be 5050"