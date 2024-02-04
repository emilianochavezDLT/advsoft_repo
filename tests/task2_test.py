from main import main

def test_is_int():
    is_int = main()
    assert isinstance(is_int, int), "should be an integer"
