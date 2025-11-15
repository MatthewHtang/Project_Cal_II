from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'matthew',
        ['matthew.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++14'],   # << FIX
    ),
]

setup(
    name='matthew',
    version='1.0',
    ext_modules=ext_modules
)
