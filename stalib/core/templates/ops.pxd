import cython

cdef extern from "<vector>" namespace "std": 
    cdef cppclass vector[T]:
        vector() except + 
        vector(vector&) except + 
        vector(size_t) except + 
        vector(size_t, T&) except + 
        T& operator[](size_t)
        void clear()
        void push_back(T&)


