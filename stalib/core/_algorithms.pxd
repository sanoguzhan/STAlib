import cython
from libcpp.vector cimport vector

cdef extern from "algorithms/sort/sort.hpp" namespace "sta":
    void bubble_sort[T](vector[T] &vec) nogil except +
    void merge_sort[T](vector[T] &vec) nogil except +
