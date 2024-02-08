from main import numpy_operations
import numpy as np

# To test on pytest, In replit I used the command:
# pytest tests/task7_tests.py



def test_array_ops_mean():
    #Calling numpy operations with an array

    #create the array first 
    arr = np.array([1, 2, 3, 4, 5])
    arr_mean, arr_sum = numpy_operations(arr)

    #assert the mean and sum of the array
    assert arr_mean == 3.0
    assert arr_sum == 15