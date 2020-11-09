==============
STALib
==============
Standard Template and algorithms library of C++ for Python with C-Python API


.. image:: https://readthedocs.org/projects/more-itertools/badge/?version=latest
  :target: https://more-itertools.readthedocs.io/en/stable/

Stalib Library includes complementary algotrithms and templates to Python's ``built-in``.
The algorithms implemented in C++ and extended to Python and compitable with Python's ``list`` objects.

############
Algorithms:
############
Sort and Search Algorithms:

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Sort Algorithms**    | `Bubble Sort`_,                                                                                                                                                                                                      |
|                        | `Merge Sort`_,                                                                                                                                                                                                       |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Templates**
| **Sequence**           | `Vector`_,                                                                                                                                                                                                      |
|                        | `List`_,                                                                                                                                                                                                       |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Getting started
===============

To get started, install the library with `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: shell

    pip install stalib

Example 
**********

Import the algorithms or templates:

.. code-block:: python

    >>> from stalib.algorithms import merge_sort
    >>> iterable = [1,9,2,4]
    >>> list(merge_sort(iterable))
    [0, 1, 2, 3]



For the full listing of functions, see the [Algorithms](#algorithms) and [Tempaltes](#templates)_.

