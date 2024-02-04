from main import int_num, float_num, string, boolean

# Task 2: Varaibles and Data Types

def test_int_num():
    assert isinstance(int_num, int)
    assert int_num == 10, "int_num is not 10"

def test_float_num():
    assert isinstance(float_num, float)
    assert float_num == 10.10, "float_num is not 10.10"

def test_string():
    assert isinstance(string, str)
    assert string == "Hello World", "string is not Hello World"

def test_boolean():
    assert isinstance(boolean, bool)
    assert boolean == True, "boolean is not True"
