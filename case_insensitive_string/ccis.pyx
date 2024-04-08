import itertools
import sys

from cpython.unicode cimport Py_UNICODE_TOLOWER
from cython.view cimport array


cdef extern from "Python.h":
	cdef Py_ssize_t PY_SSIZE_T_MAX

"""
#define ADJUST_INDICES(start, end, len)         \
    if (end > len)                              \
        end = len;                              \
    else if (end < 0) {                         \
        end += len;                             \
        if (end < 0)                            \
            end = 0;                            \
    }                                           \
    if (start < 0) {                            \
        start += len;                           \
        if (start < 0)                          \
            start = 0;                          \
}
"""

cdef class CaseInsensitiveString(object):

	cdef readonly str _s # how does this work without exposing to python
	cdef Py_ssize_t hash

	def __cinit__(self):
		self.hash = -1

	def __init__(self, str s):
		self._s = s

	def __str__(self):
		return self._s

	def __repr__(self):
		return "CaseInsensitiveString(" + repr(self._s) + ")"

	def __hash__(self):
		# based on https://svn.python.org/projects/python/trunk/Objects/unicodeobject.c
		"""
		cdef Py_ssize_t l
		cdef int i
		cdef Py_ssize_t x

		if self.hash != -1:
			return self.hash

		l = len(self._s)
		i = 0
		x = Py_UNICODE_TOLOWER(self._s[0])
		l -= 1
		while l >= 0:
			x = (1000003*x) ^ <Py_ssize_t>Py_UNICODE_TOLOWER(self._s[i])
			i += 1
			l -= 1
		x ^= len(self._s)
		if x == -1:
			x = -2
		self.hash = x
		return x;
		"""
		# use https://github.com/python/cpython/blob/b2e5794870eb4728ddfaafc0f79a40299576434f/Python/pyhash.c instead

		if self.hash != -1:
			return self.hash

		self.hash = hash(self._s.lower())
		return self.hash

	def __richcmp__(CaseInsensitiveString x, CaseInsensitiveString y, int op):

		if op == 0: # Py_LT
			return CaseInsensitiveString._lt__(x, y)
		elif op == 1: # Py_LE
			return CaseInsensitiveString._le__(x, y)
		elif op == 2: # Py_EQ
			return CaseInsensitiveString._eq__(x, y)
		elif op == 3: # Py_NE
			return CaseInsensitiveString._ne__(x, y)
		elif op == 4: # Py_GT
			return CaseInsensitiveString._gt__(x, y)
		elif op == 5: # Py_GE
			return CaseInsensitiveString._ge__(x, y)
		else:
			assert False

	def _eq__(x, y):
		#if x is y:
		#	return True

		if len(x._s) != len(y._s):
			return False

		for i, j in zip(x._s, y._s):
			if i.lower() != j.lower():
				return False
		return True

	def _ne__(x, y):

		#if x is y:
		#	return True

		for i, j in zip(x._s, y._s):
			if i.lower() != j.lower():
				return True
		return len(x._s) != len(y._s)

	def _lt__(x, y):
		assert False

	def _gt__(x, y):
		assert False

	def _le__(x, y):
		assert False

	def _ge__(x, y):
		assert False

	def __len__(self):
		return len(self._s)

	def __add__(x, y):
		return CaseInsensitiveString(x._s + y._s)

	def __mul__(x, y):
		if isinstance(y, int):
			return CaseInsensitiveString(x._s * y)
		else:
			return CaseInsensitiveString(y._s * x)

	def __contains__(self, str x) -> int:
		return self.find(x) != -1

	cpdef int index(self, str sub, Py_ssize_t start=0, Py_ssize_t end=PY_SSIZE_T_MAX) except? -1:
		cdef int result = self.find(sub, start, end)
		if result < 0:
			raise ValueError("substring not found")
			return -1
		return result

	cpdef int find(self, str sub, Py_ssize_t start=0, Py_ssize_t end=PY_SSIZE_T_MAX):
		cdef Py_ssize_t len1 = len(self._s)
		cdef Py_ssize_t len2 = len(sub)

		if end > len1:
			end = len1
		elif end < 0:
			end += len1
			if end < 0:
				end = 0
		if start < 0:
			start += len1
			if start < 0:
				start = 0

		if len(sub) > end - start:
			return -1

		cdef str sublower = sub.lower()

		# use ring buffer of length len(sub) where lowercase characters are added
		for i in range(start, end-len2+1): # both cpu and memory usage can be improved
			if self._s[i:i+len2].lower() == sublower:
				return i

		return -1

	cpdef str startswith(self, str prefix):

		if len(self._s) < len(prefix):
			return False

		for i, j in zip(self._s, prefix):
			if i.lower() != j.lower():
				return False
		return True

	cpdef str endswith(self, str suffix):

		if len(self._s) < len(suffix):
			return False

		for i, j in zip(reversed(self._s), reversed(suffix)):
			if i.lower() != j.lower():
				return False
		return True
