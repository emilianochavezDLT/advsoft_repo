from main import numpy_operations
import numpy as np


def test_array_ops():
    #Calling numpy operations with an array

    #create the array first 
    arr = np.array([1, 2, 3, 4, 5])
    arr_mean, arr_sum = numpy_operations(arr)

    #assert the mean and sum of the array
    assert arr_mean == 3.0
    assert arr_sum == 15