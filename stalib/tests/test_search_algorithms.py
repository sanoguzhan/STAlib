import pytest
from stalib.algorithms import buble_sort, merge_sort, quick_sort, binary_search
import time
import random
from stalib.utils.helpers import speed_test


@pytest.mark.parametrize(
    "sorted_list,token",[([1,4,8,10,22,34],22)]
)
def test_binary_search(
    sorted_list,
    token
):
    """
    Test for Bubble search algorithm
        Test for list with int, string, float types
    """

    assert binary_search(sorted_list, 22) == 4
    assert binary_search(["a", "g", "p", "x"], "g") == 1
    assert binary_search([1.2, 1.4, 2.1, 2.199, 3.29, 4.2],3.29) == 4
