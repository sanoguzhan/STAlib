from stalib.core cimport _algorithms
from stalib.errors import STALibValidationError
from libcpp.vector cimport vector
from libcpp.string cimport string
import cython 


cdef class Typed:
    """
    Type Casting Cython Class
    for data casting and reference input for C++ functions
    Data typed for function templates defined here for compilation
    """
    cdef:
        list __data
    def __cinit__(self, ll):
        self.__data = ll

    cpdef MergeSort(self):
        typed = Typed.validate(self.__data)
        if typed is str:
            return Typed._MergeSortString([i.encode('utf-8') for i in self.__data])
        elif typed is int:
            return Typed._MergeSortLong(self.__data)
        elif typed is float:
            return Typed._MergeSortDouble(self.__data)


    cpdef BubbleSort(self):
        typed = Typed.validate(self.__data)
        if typed is str:
            return Typed._BubbleSortString([i.encode('utf-8') for i in self.__data])
        elif typed is int:
            return Typed._BubbleSortLong(self.__data)
        elif typed is float:
            return Typed._BubbleSortDouble(self.__data)
    
    cpdef QuickSort(self):
        typed = Typed.validate(self.__data)
        if typed is str:
            return Typed._QuickSortString([i.encode('utf-8') for i in self.__data])
        elif typed is int:
            return Typed._QuickSortLong(self.__data)
        elif typed is float:
            return Typed._QuickSortDouble(self.__data)

    @staticmethod
    cdef _QuickSortString(vector[string] _data):
        with nogil:
            _algorithms.quick_sort(_data)
        return [v.decode("utf-8") for v in _data]

    @staticmethod
    cdef _QuickSortLong(vector[long] _data):
        with nogil:
            _algorithms.quick_sort(_data)
        return _data

    @staticmethod
    cdef _QuickSortDouble(vector[double] _data):
        with nogil:
            _algorithms.quick_sort(_data)
        return _data

    @staticmethod
    cdef _MergeSortString(vector[string] _data):
        with nogil:
            _algorithms.merge_sort(_data)
        return [v.decode("utf-8") for v in _data]

    @staticmethod
    cdef _MergeSortLong(vector[long] _data):
        with nogil:
            _algorithms.merge_sort(_data)
        return _data

    @staticmethod
    cdef _MergeSortDouble(vector[double] _data):
        with nogil:
            _algorithms.merge_sort(_data)
        return _data

    @staticmethod
    cdef _BubbleSortString(vector[string] _data):
        with nogil:
            _algorithms.bubble_sort(_data)
        return [v.decode("utf-8") for v in _data]

    @staticmethod
    cdef _BubbleSortLong(vector[long] _data):
        with nogil:
            _algorithms.bubble_sort(_data)
        return _data

    @staticmethod
    cdef _BubbleSortDouble(vector[double] _data):
        with nogil:
            _algorithms.bubble_sort(_data)
        return _data
    @staticmethod
    cdef validate(list ll):
        """
        Finds the type of all element in the list
        :param:
            ll: list which may contain any type of elements"""
        it = iter(ll)
        first_type = type(next(it))
        return first_type if all( (type(i) is first_type) for i in it) else False

  