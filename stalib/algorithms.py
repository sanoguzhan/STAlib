from typing import List, Any, Dict, Tuple, Union
from engine import Typed


"""
STAlib Algorithms Python Entrypoint
"""
def buble_sort(ll: List[Any]):
    return Typed(ll).BubbleSort()


def merge_sort(ll: List[Any]):
    return Typed(ll).MergeSort()

def quick_sort(ll: List[Any]):
    return Typed(ll).QuickSort()

def binary_search(ll: List[Any], token: Union[str, int, float]):
    return Typed(ll).BinarySearch(token)