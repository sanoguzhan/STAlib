import cython
from libcpp.vector cimport vector

cdef extern from "<vector>" namespace "std": 
    cdef cppclass vector[T]:
        vector() except + 
        vector(vector&) except + 
        vector(size_t) except + 
        vector(size_t, T&) except + 
        T& operator[](size_t)
        void clear()
        void push_back(T&)
        cppclass iterator:
            T& operator*()
            iterator operator++()
            iterator operator--()
            iterator operator+(size_t)
            iterator operator-(size_t)
            bint operator==(iterator)
            bint operator!=(iterator)
            bint operator<(iterator)
            bint operator>(iterator)
            bint operator<=(iterator)
            bint operator>=(iterator)
