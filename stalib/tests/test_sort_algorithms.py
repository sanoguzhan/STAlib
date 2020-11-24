import pytest
from stalib.algorithms import buble_sort, merge_sort, quick_sort
import time
import random
from stalib.utils.helpers import speed_test

def test_bubble_sort(
    Integer,
    String,
    Float
):
    """
    Test for buble sort Algortihm
    input data:
        test_input_{PythonObject} test input Python list contains Python int, float, string
        expected_{PythonObject} expected output Python list Python int, float, string
    """

    assert buble_sort(Integer.get("input")) == Integer.get("expected")
    assert buble_sort(String.get("input")) == String.get("expected")
    assert buble_sort(Float.get("input")) == Float.get("expected")



def test_merge_sort(Integer,
    String,
    Float):

    """
    Test for merge sort Algortihm
    input data:
        test_input_{PythonObject}:
             test input Python list contains Python int, float, string
        expected_{PythonObject}:
             expected output Python list Python int, float, string
    """
    assert merge_sort(Integer.get("input")) == Integer.get("expected")
    assert merge_sort(String.get("input")) == String.get("expected")
    assert merge_sort(Float.get("input")) == Float.get("expected")


def test_quick_sort(Integer,
    String,
    Float):

    """
    Test for merge sort Algortihm
    input data:
        test_input_{PythonObject}:
             test input Python list contains Python int, float, string
        expected_{PythonObject}:
             expected output Python list Python int, float, string
    """
    assert quick_sort(Integer.get("input")) == Integer.get("expected")
    assert quick_sort(String.get("input")) == String.get("expected")
    assert quick_sort(Float.get("input")) == Float.get("expected")


def test_compare_performance():
    """
    Test for sorting algorithms with Python core Sort Algorithms (timsort)
    """
    random_list = [i * random.randint(1,99) for i in range(10**4)]
    sorted_list = sorted(random_list)
    assert quick_sort(random_list) == sorted_list
    assert merge_sort(random_list) == sorted_list
    assert buble_sort(random_list) == sorted_list
    