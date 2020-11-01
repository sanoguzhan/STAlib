from stalib.core cimport _algorithms
from stalib.errors import STALibValidationError
from libcpp.vector cimport vector
from libcpp.string cimport string
import cython 


ctypedef fused any:
    cython.int
    string


cpdef _sort_bubble(list ll):
    """
    Entry point for C++ functions"""
    typed = validate(ll)
    if not type:
        raise STALibValidationError
    
    if typed is int:    
        return BubbleSort._long(ll)
    elif typed is float:
        return BubbleSort._double(ll)

cdef validate(list ll):
    """
    Finds the type of all element in the list
    :param:
        ll: list which may contain any type of elements"""
    it = iter(ll)
    first_type = type(next(it))
    return first_type if all( (type(i) is first_type) for i in it) else False


cdef class BubbleSort:
    """
    Bubble Sort Cython Class
    for data casting and reference input for C++ functions
    Data typed for function templates defined here for compilation
    """
    @staticmethod
    cdef _long(vector[long] vv):
        with nogil:     
            _algorithms.bubble_sort(vv)
        return vv
    @staticmethod
    cdef _double(vector[double] vv):
        with nogil:     
            _algorithms.bubble_sort(vv)
        return vv