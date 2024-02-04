from main import int_number, float_number, string, boolean

# Task 2: Varaibles and Data Types
def test_is_int():
    is_int = int_number()
    assert isinstance(is_int, int), "should be an integer"

def test_if_10():
    is_10 = int_number()
    assert is_10 == 10, "should be 10"

def test_is_float():
    is_float = float_number()
    assert isinstance(is_float, float), "should be a float"

def test_if_10_10():
    is_10_10 = float_number()
    assert is_10_10 == 10.10, "should be 10.10"

def test_is_string():
    is_string = string()
    assert isinstance(is_string, str), "should be a string"

def test_is_hello_world():
    is_hello_world = string()
    assert is_hello_world == "Hello World", "should be Hello World"

def test_is_boolean():
    is_boolean = boolean()
    assert isinstance(is_boolean, bool), "should be a boolean"

def test_is_true():
    is_true = boolean()
    assert is_true == True, "should be True"
