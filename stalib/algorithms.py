from typing import List, Any, Dict, Tuple
import sys;print(sys.path)
from engine import Typed

def buble_sort(ll: List[Any]):
    return Typed(ll).BubbleSort()


def merge_sort(ll: List[Any]):
    return Typed(ll).MergeSort()

def quick_sort(ll: List[Any]):
    return Typed(ll).QuickSort()