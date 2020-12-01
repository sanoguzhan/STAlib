
# STALib


![build](https://github.com/sanoguzhan/STAlib/workflows/build/badge.svg)
![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)
[![unstable](http://badges.github.io/stability-badges/dist/unstable.svg)](http://github.com/badges/stability-badges)


Standard Template and algorithms library of C++ for Python with C-Python API

Stalib Library includes complementary algotrithms and templates to Python's ``built-in``.
The algorithms implemented in C++ and extended to Python and compitable with Python's ``list`` objects.


Algorithms:




| Name          | Type          | Worst-case Performance                   | Module
| ------------- |:-------------:| --------------------------------:|-------------:|
| [Buble Sort](https://en.wikipedia.org/wiki/Bubble_sort)    |  Sort       | O(n^2)|algorithms
| [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)     | Sort      |   O(nlogn) |algorithms
| [Quick Sort](https://en.wikipedia.org/wiki/Quicksort)| Sort    |    O(n^2) |algorithms
| [Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm)| Search    |     *O(Logn) |algorithms



*Sorted Array

------
## Getting started


To get started, install the library with [pip](https://pip.pypa.io/en/stable/)

```bash
    pip install stalib
```
  

## Example 


Import the algorithms or templates:

```python

    >>> from stalib.algorithms import merge_sort
    >>> iterable = [1,9,2,4]
    >>> list(merge_sort(iterable))
    [1, 2, 4, 9]

```

For the full listing of functions, see [stalib](https://pypi.org/search/?q=stalib)

