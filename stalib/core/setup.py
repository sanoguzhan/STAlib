
import setuptools
import os
from distutils.core import setup
from distutils.extension import Extension
setuptools.dist.Distribution().fetch_build_eggs(['Cython'])
from Cython.Build import cythonize 





ext_lib_path = 'stalib/core/algorithms'

dir_sort = os.path.join(ext_lib_path, "sort")


dir_search = os.path.join(ext_lib_path, "search")





ext_modules=[

   Extension(name="engine", sources=["stalib/core/engine.pyx", 
   "stalib/core/algorithms/sort/sort.cpp", 
   "stalib/core/algorithms/search/search.cpp", 
   ],
        include_dirs=[dir_sort, dir_search],
        language="c++",
        extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp']),

]


setup(
  ext_modules = cythonize(ext_modules, 
  language_level=3,
  ),
)