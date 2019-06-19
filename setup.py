from setuptools import setup, Extension
from io import open

try:
	from Cython.Build import cythonize
	USE_CYTHON = True
except ImportError:
	USE_CYTHON = False

if USE_CYTHON:
	SOURCES = [
		"case_insensitive_string/ccis.pyx",
		
	]
else:
	SOURCES = [
		"case_insensitive_string/ccis.c",
	]

extensions = [
	Extension("ccis", sources=SOURCES),
	Extension("cis", sources=["case_insensitive_string/cis.py"])
]

if USE_CYTHON:
	extensions = cythonize(extensions)

with open("README.md", "r", encoding="utf-8") as fr:
	long_description = fr.read()

setup(
	author="Dobatymo",
	name="case-insensitive-string",
	version="0.0.1",
	description="A case-insensitive string class",
	long_description=long_description,
	long_description_content_type="text/markdown",
	ext_modules=extensions,
	python_requires=">=2.7",
	use_2to3=False
)
