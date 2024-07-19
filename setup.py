from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("ccis", sources=["case_insensitive_string/ccis.pyx"]),
    Extension("cis", sources=["case_insensitive_string/cis.py"]),
]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
