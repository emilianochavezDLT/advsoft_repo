from main import int_number, float_number, string, boolean

def test_is_int():
    is_int = int_number()
    assert isinstance(is_int, int), "should be an integer"

