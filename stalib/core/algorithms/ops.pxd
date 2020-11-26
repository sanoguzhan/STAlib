import cython
from libcpp.vector cimport vector

cdef extern from "algorithms/sort/sort.hpp" namespace "sta":
    void bubble_sort[T](vector[T] &vec) nogil except +
    void merge_sort[T](vector[T] &vec) nogil except +
    void quick_sort[T](vector[T] &vec, int low, int high, int pivot) nogil except +


cdef extern from "algorithms/search/search.hpp":
    int binary_search[T](vector[T] &vec, T token) nogil except +