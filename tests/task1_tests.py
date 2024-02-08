from main import hello_Replit

# To test on pytest, In replit I used the command:
# pytest tests/task1_tests.py

# This is the test case for the hello_Replit function
# Task 1: Introduction to Replit
def test_hello_replit():
    assert hello_Replit() == "Hello Replit!"