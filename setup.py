from distutils.core import setup
from Cython.Build import cythonize

setup(
	name="case-insensitive-string",
	version="0.0.1",
	ext_modules=cythonize(["cis.py", "ccis.pyx"])
)
