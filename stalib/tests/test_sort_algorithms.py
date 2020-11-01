import pytest
from stalib.algorithms import buble_sort
import time
import random

@pytest.mark.parametrize(
    "test_input_int,expected_int", [([1,0,90,5,4,2],
     [0,1,2,4,5,90])]
)

@pytest.mark.parametrize(
    "test_input_float,expected_float", [([1.0,0.9,90.2,5.4,4.2,2.1,2.3,], 
    [0.9, 1.0, 2.1, 2.3, 4.2, 5.4, 90.2])]
)

def test_bubble_sort(test_input_int,
    test_input_float, expected_int, expected_float):
    """
    Test for buble sort Algortihm
    """

    assert buble_sort(test_input_int) == expected_int
    assert buble_sort(test_input_float) == expected_float


