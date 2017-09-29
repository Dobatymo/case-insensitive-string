#!python3
from __future__ import absolute_import, unicode_literals

from typing import Tuple, Any

class CaseInsensitiveString(object):
	"""Case insensitive string """

	def __init__(self, s):
		self._s = s

	def __repr__(self):
		return "CaseInsensitiveString({})".format(repr(self._s))

	def __str__(self):
		return self._s

	def __eq__(self, other) -> bool:
		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() == other._s.lower()
		else:
			return self._s.lower() == other.lower()

	def __ne__(self, other) -> bool:
		return self._s.lower() != other._s.lower()

	def __lt__(self, other) -> bool:
		return self._s.lower() < other._s.lower()

	def __le__(self, other) -> bool:
		return self._s.lower() <= other._s.lower()

	def __gt__(self, other) -> bool:
		return self._s.lower() > other._s.lower()

	def __ge__(self, other) -> bool:
		return self._s.lower() >= other._s.lower()

	def __add__(self, other: str):
		return CaseInsensitiveString(self._s + other._s)

	def __mul__(self, other: int):
		return CaseInsensitiveString(self._s * other)

	def __mod__(self, other: Any):
		return CaseInsensitiveString(self._s % other)

	def __len__(self):
		return len(self._s)

	def __iter__(self):
		return iter(self._s)

	def __hash__(self):
		return hash(self._s.lower())

	def __getitem__(self, key: int):
		return CaseInsensitiveString(self._s[key])

	def __contains__(self, other):
		return other._s.lower() in self._s.lower()

	def capitalize(self):
		return CaseInsensitiveString(self._s.capitalize())

	def casefold(self):
		return CaseInsensitiveString(self._s.casefold())

	def center(self, *args, **kwargs):
		return CaseInsensitiveString(self._s.center(*args, **kwargs))

	def count(self, sub, *args, **kwargs) -> int:
		return self._s.lower().count(sub.lower(), *args, **kwargs)

	def encode(self, *args, **kwargs) -> bytes:
		return self._s.encode(*args, **kwargs)

	def endswith(self, suffix, *args, **kwargs) -> bool:
		if isinstance(suffix, CaseInsensitiveString):
			return self._s.lower().endswith(suffix._s.lower(), *args, **kwargs)
		else:
			return self._s.lower().endswith(suffix.lower(), *args, **kwargs)

	def expandtabs(*args, **kwargs):
		return CaseInsensitiveString(self._s.expandtabs(*args, **kwargs))

	def find(self, sub, *args, **kwargs) -> int:
		return self._s.lower().find(sub.lower(), *args, **kwargs)

	def format(self, *args, **kwargs):
		return CaseInsensitiveString(self._s.format(*args, **kwargs))

	def format_map(self, mapping):
		return CaseInsensitiveString(self._s.format_map(mapping))

	def index(self, sub, *args, **kwargs) -> int:
		return self._s.lower().index(sub.lower(), *args, **kwargs)

	def isalnum(self) -> bool:
		return self._s.isalnum()

	def isalpha(self) -> bool:
		return self._s.isalpha()

	def isdecimal(self) -> bool:
		return self._s.isdecimal()

	def isdigit(self) -> bool:
		return self._s.isdigit()

	def isidentifier(self) -> bool:
		return self._s.isidentifier()

	def islower(self) -> bool:
		return self._s.islower()

	def isnumeric(self) -> bool:
		return self._s.isnumeric()

	def isprintable(self) -> bool:
		return self._s.isprintable()

	def isspace(self) -> bool:
		return self._s.isspace()

	def istitle(self) -> bool:
		return self._s.istitle()

	def isupper(self) -> bool:
		return self._s.isupper()

	def join(self, iterable):
		return CaseInsensitiveString(self._s.join(iterable))

	def ljust(self, width, *args, **kwargs):
		return CaseInsensitiveString(self._s.ljust(width, *args, **kwargs))

	def lower(self):
		return CaseInsensitiveString(self._s.lower())

	def lstrip(self, chars=None):
		if chars is None:
			return CaseInsensitiveString(self._s.lstrip())
		else:
			raise NeedsOwnImplementation

	@staticmethod
	def maketrans(*args, **kwargs) -> dict: # create case insensitive dict here?
		return self._s.maketrans(*args, **kwargs)

	def partition(self, sep) -> Tuple:
		pos = self.find(sep)
		if pos == -1:
			return (self, CaseInsensitiveString(""), CaseInsensitiveString("")) # self should be immutable
		else:
			return (self._s[0:pos], sep, self._s[pos+len(sep):])

	def replace(self, old, new, count=None):
		raise NeedsOwnImplementation

	def replace(self, old, new, count=-1):

		if not old and not new:
			return self

		start = 0
		ret = self._s

		while count != 0:

			if old:
				start = ret.lower().find(old.lower(), start)
			if start >= 0:
				ret = ret[:start] + new + ret[start + len(old):]
				if not old:
					start += 1
					if start + 1 >= len(ret):
						break

				start += len(new)
				count -= 1
			else:
				break

		return CaseInsensitiveString(ret)

	def rfind(self, sub, *args, **kwargs) -> int:
		return self._s.lower().rfind(sub.lower(), *args, **kwargs)

	def rindex(self, sub, *args, **kwargs) -> int:
		return self._s.lower().rindex(sub.lower(), *args, **kwargs)

	def rjust(self, width, *args, **kwargs):
		return CaseInsensitiveString(self._s.rjust(width, *args, **kwargs))

	def rpartition(self, sep) -> Tuple:
		pos = self.rfind(sep)
		if pos == -1:
			return (CaseInsensitiveString(""), CaseInsensitiveString(""), self) # self should be immutable
		else:
			return (self._s[0:pos], sep, self._s[pos+len(sep):])

	def rsplit(self, sep=None, maxsplit=-1):
		if sep is None:
			return list(CaseInsensitiveString(s) for s in self._s.rsplit(sep, maxsplit))
		else:
			raise NeedsOwnImplementation

	def rstrip(self, chars=None):
		if chars is None:
			return CaseInsensitiveString(self._s.rstrip())
		else:
			raise NeedsOwnImplementation

	def split(self, sep=None, maxsplit=-1):
		if sep is None:
			return list(CaseInsensitiveString(s) for s in self._s.split(sep, maxsplit))
		else:
			if not isinstance(sep, str):
				raise TypeError("must be str or None, not {}".format(type(sep)))
			if sep == "":
				raise ValueError("empty separator")

			ret = []
			pos = 0
			c = maxsplit
			while c != 0:
				newpos = self.find(sep, pos)
				if newpos == -1:
					break
				else:
					part = self._s[pos:newpos]
					ret.append(CaseInsensitiveString(part))
					pos = newpos + len(sep)
					c -= 1
			ret.append(CaseInsensitiveString(self._s[pos:]))
			return ret

	def splitlines(self, *args, **kwargs) -> list:
		return list(CaseInsensitiveString(line) for line in self._s.splitlines(*args, **kwargs))

	def startswith(self, prefix, *args, **kwargs) -> bool:
		if isinstance(prefix, CaseInsensitiveString):
			return self._s.lower().startswith(prefix._s.lower(), *args, **kwargs)
		else:
			return self._s.lower().startswith(prefix.lower(), *args, **kwargs)

	def strip(self, chars=None):
		if chars is None:
			return CaseInsensitiveString(self._s.strip())
		else:
			chars = "".join(set(chars.lower()) | set(chars.upper))
			return CaseInsensitiveString(self._s.strip(chars))

	def swapcase(self):
		return CaseInsensitiveString(self._s.swapcase())

	def title(self):
		return CaseInsensitiveString(self._s.title())

	def translate(self, table):
		return CaseInsensitiveString(self._s.translate(table))

	def upper(self):
		return CaseInsensitiveString(self._s.upper())

	def zfill(self, width):
		return CaseInsensitiveString(self._s.lower().zfill(width))

CIS = CaseInsensitiveString

from libs.utils_test import TestCaseEx
class CaseInsensitiveStringTest(TestCaseEx):

	def test_equal(self):
		self.assertEqual(CIS("a"), CIS("A"))
		self.assertEqual(CIS("A"), CIS("a"))
		self.assertEqual(CIS("Asd"), CIS("asD"))
		self.assertEqual(CIS("asd"), CIS("ASD"))
		self.assertNotEqual(CIS("a"), CIS("b"))
		self.assertNotEqual(CIS("a"), CIS("as"))

	def test_hash(self):
		self.assertEqual(hash(CIS("a")), hash(CIS("A")))
		self.assertEqual(hash(CIS("A")), hash(CIS("a")))
		self.assertEqual(hash(CIS("Asd")), hash(CIS("asD")))
		self.assertEqual(hash(CIS("asd")), hash(CIS("ASD")))
		self.assertNotEqual(hash(CIS("a")), hash(CIS("b")))
		self.assertNotEqual(hash(CIS("a")), hash(CIS("as")))

	def test_endswith(self):
		self.assertTrue(CIS("asd").endswith(CIS("d")))
		self.assertTrue(CIS("asd").endswith(CIS("sd")))
		self.assertTrue(CIS("asd").endswith(CIS("asd")))
		self.assertTrue(CIS("ASD").endswith(CIS("d")))
		self.assertTrue(CIS("ASD").endswith(CIS("sd")))
		self.assertTrue(CIS("ASD").endswith(CIS("asd")))
		self.assertFalse(CIS("asd").endswith(CIS("a")))
		self.assertFalse(CIS("ASD").endswith(CIS("a")))
		self.assertFalse(CIS("asd").endswith(CIS("A")))
		self.assertFalse(CIS("ASD").endswith(CIS("A")))

	def test_lower(self):

		for s in ("A", "a", "aA"):
			self.assertEqual(s.lower(), CIS(s).lower())

	def test_replace(self):
		result = CIS("").replace("", "")
		truth = ""
		self.assertEqual(truth, result)

		result = CIS("").replace("asd", "")
		truth = ""
		self.assertEqual(truth, result)

		result = CIS("").replace("asd", "qwe")
		truth = ""
		self.assertEqual(truth, result)

		result = CIS("asd").replace("", "")
		truth = "asd"
		self.assertEqual(truth, result)

		result = CIS("asd").replace("asd", "")
		truth = ""
		self.assertEqual(truth, result)

		result = CIS("").replace("", "X")
		truth = "X"
		self.assertEqual(truth, result)

		result = CIS("asd").replace("", "X")
		truth = "XaXsXd"
		self.assertEqual(truth, result)

		result = CIS("asdFGHjkl").replace("fgh", "123")
		truth = "asd123jkl"
		self.assertEqual(truth, result)

		result = CIS("aaAA").replace("a", "b")
		truth = "bbbb"
		self.assertEqual(truth, result)

		result = CIS("aaAA").replace("a", "b", 2)
		truth = "bbAA"
		self.assertEqual(truth, result)

		result = CIS("-aa+aaaa+aa-").replace("aa", "a", 2)
		truth = "-a+aaa+aa-"
		self.assertEqual(truth, result)

if __name__ == "__main__":
	import unittest
	unittest.main()
