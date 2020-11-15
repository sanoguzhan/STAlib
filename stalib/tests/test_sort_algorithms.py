import pytest
from stalib.algorithms import buble_sort, merge_sort
import time
import random

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

