
import setuptools
import os
from re import sub
from distutils.core import setup
from distutils.extension import Extension
from distutils.command.sdist import sdist as _sdist
from distutils.errors import DistutilsSetupError
from distutils.command.build_clib import build_clib
from logging import log

from stalib import __version__
setuptools.dist.Distribution().fetch_build_eggs(['Cython'])
from Cython.Distutils import build_ext
from Cython.Build import cythonize 


_path = str("requirements.txt")
with open(_path) as f:
    required = f.read().splitlines()




cmdclass = {}
ext_lib_path = 'stalib/core/algorithms'

dir_sort = os.path.join(ext_lib_path, "sort")

dir_search = os.path.join(ext_lib_path, "search")





macros = None

ext_libraries = [['sort', {
               'sources': [os.path.join(dir_sort, 'sort.cpp'),],
               'include_dirs': [dir_sort],
               'macros': macros,
                'cflags' : ["-std=c++11", ]
               }
],
['search', {
               'sources': [os.path.join(dir_search, "search.cpp")],
               'include_dirs': [dir_search],
               'macros': macros,
                'cflags' : ["-std=c++11",]
               }
]]

def get_long_description():
    readme = open('README.md').read()
    version_lines = []
    with open('docs/versions.rst') as infile:
        next(infile)
        for line in infile:
            version_lines.append(line)
    version_history = '\n'.join(version_lines)
    version_history = sub(r':func:`([a-zA-Z0-9._]+)`', r'\1', version_history)

    return readme + '\n\n' + version_history

ext_modules=[

   Extension(name="engine", sources=["stalib/core/engine.pyx", 
   "stalib/core/algorithms/sort/sort.cpp", 
   "stalib/core/algorithms/search/search.cpp", 
   ],
    include_dirs=[dir_sort, dir_search],
    language="c++",
   )
]


setup(
  name = "stalib",
  version=__version__,
  package_data={'': ['*.pyx', '*.pxd', '*.h', '*.cpp', '*.hpp']},
  packages=setuptools.find_packages(exclude=["tests/*"]),
  install_requires=required,
  include_package_data=True,
  ext_modules = cythonize(ext_modules, 
  language_level=3,
  ),
  url="https://github.com/sanoguzhan/STAlib",
  long_description=get_long_description(),
  author='Oguzhan San',
  author_email='sanoguzhan@hotmail.com',
  license='MIT',
  long_description_content_type='text/markdown',
  libraries=ext_libraries,
  cmdclass = {'build_ext': build_ext},
  setup_requires=['cython', 'pytest-runner'],
  tests_require = ['pytest'],
  test_suite ='tests',
  python_requires='>=3.0',
    classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
    keywords=[
        'Template',
        'Cython',
        'Algorithms',
        'C++',
        'Sort',
        'Search',
        'Data Containers',
    ],
)