from __future__ import absolute_import, division, print_function, unicode_literals

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from typing import Tuple, Any

class CaseInsensitiveString(object):
	"""Case insensitive string """

	def __init__(self, s):
		self._s = s

	def __repr__(self):
		return "CaseInsensitiveString({})".format(repr(self._s))

	def __str__(self):
		return self._s

	def __eq__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() == other._s.lower()
		else:
			return self._s.lower() == other.lower()

	def __ne__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() != other._s.lower()
		else:
			return self._s.lower() != other.lower()

	def __lt__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() < other._s.lower()
		else:
			return self._s.lower() < other.lower()

	def __le__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() <= other._s.lower()
		else:
			return self._s.lower() <= other.lower()

	def __gt__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() > other._s.lower()
		else:
			return self._s.lower() > other.lower()

	def __ge__(self, other):
		# type: (Any, ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return self._s.lower() >= other._s.lower()
		else:
			return self._s.lower() >= other.lower()

	def __add__(self, other):
		# type: (CIS, ) -> CIS

		if isinstance(other, CaseInsensitiveString):
			return CaseInsensitiveString(self._s + other._s)
		else:
			return CaseInsensitiveString(self._s + other)

	def __mul__(self, other):
		# type: (int, ) -> CIS

		return CaseInsensitiveString(self._s * other)

	def __mod__(self, other):
		# type: (Tuple, ) -> CIS

		return CaseInsensitiveString(self._s % other)

	def __len__(self):
		return len(self._s) # the length of the lowercase version might be different

	def __iter__(self):
		# type: () -> Interable[CIS]

		for c in self._s:
			yield CaseInsensitiveString(c)

	def __hash__(self):
		# type: () -> int

		return hash(self._s.lower())

	def __getitem__(self, key): # key can be slice object also
		# type: (int, ) -> CIS

		return CaseInsensitiveString(self._s[key])

	def __contains__(self, other):
		# type: (Union[str, CIS], ) -> bool

		if isinstance(other, CaseInsensitiveString):
			return other._s.lower() in self._s.lower()
		else:
			return other.lower() in self._s.lower()

	def capitalize(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.capitalize())

	def casefold(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.casefold())

	def center(self, width, fillchar=" "):
		# type: (int, str) -> CIS

		return CaseInsensitiveString(self._s.center(width, fillchar))

	def count(self, sub, start=None, end=None):
		# type: (Union[str, CIS], ) -> int

		if isinstance(sub, CaseInsensitiveString):
			return self._s.lower().count(sub._s.lower(), start, end)
		else:
			return self._s.lower().count(sub.lower(), start, end)

	def encode(self, encoding="utf-8", errors="strict"):
		# type: (str, str) -> bytes

		return self._s.encode(encoding, errors)

	def endswith(self, suffix, start=None, end=None):
		# type: (Union[str, CIS], ) -> bool

		if isinstance(suffix, CaseInsensitiveString):
			return self._s.lower().endswith(suffix._s.lower(), start, end)
		else:
			return self._s.lower().endswith(suffix.lower(), start, end)

	def expandtabs(self, tabsize=8):
		# type: (int, ) -> CIS

		return CaseInsensitiveString(self._s.expandtabs(tabsize))

	def find(self, sub, start=None, end=None):
		# type: (Union[str, CIS], ) -> int

		if isinstance(sub, CaseInsensitiveString):
			return self._s.lower().find(sub._s.lower(), start, end)
		else:
			return self._s.lower().find(sub.lower(), start, end)

	def format(self, *args, **kwargs):
		# type: (*Any, **Any) -> CIS

		return CaseInsensitiveString(self._s.format(*args, **kwargs))

	def format_map(self, mapping):
		# type: (Mapping, ) -> CIS

		return CaseInsensitiveString(self._s.format_map(mapping))

	def index(self, sub, start=None, end=None):
		# type: (Union[str, CIS], ) -> int

		if isinstance(sub, CaseInsensitiveString):
			return self._s.lower().index(sub._s.lower(), start, end)
		else:
			return self._s.lower().index(sub.lower(), start, end)

	def isalnum(self):
		# type: () -> bool

		return self._s.isalnum()

	def isalpha(self):
		# type: () -> bool

		return self._s.isalpha()

	def isdecimal(self):
		# type: () -> bool

		return self._s.isdecimal()

	def isdigit(self):
		# type: () -> bool
		return self._s.isdigit()

	def isidentifier(self):
		# type: () -> bool

		return self._s.isidentifier()

	def islower(self):
		# type: () -> bool

		return self._s.islower()

	def isnumeric(self):
		# type: () -> bool

		return self._s.isnumeric()

	def isprintable(self):
		# type: () -> bool

		return self._s.isprintable()

	def isspace(self):
		# type: () -> bool

		return self._s.isspace()

	def istitle(self):
		# type: () -> bool

		return self._s.istitle()

	def isupper(self):
		# type: () -> bool

		return self._s.isupper()

	def join(self, iterable):
		# type: (Iterable, ) -> CIS

		return CaseInsensitiveString(self._s.join(iterable))

	def ljust(self, width, fillchar=" "):
		# type: (int, str) -> CIS

		return CaseInsensitiveString(self._s.ljust(width, fillchar))

	def lower(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.lower())

	def lstrip(self, chars=None):
		# type: (CIS, ) -> CIS

		if chars is None:
			return CaseInsensitiveString(self._s.lstrip()) # only strips case insensitive whitespace anyway

		if isinstance(chars, CaseInsensitiveString):
			cs = set(chars)
		else:
			cs = set(c.lower() for c in chars)

		i = 0
		for c in self:
			if c in cs:
				i += 1
			else:
				break

		return self[i:]

	@staticmethod
	def maketrans(x, y=None, z=None): # create case insensitive dict here?
		# type: () -> dict
		return str.maketrans(x, y, z)

	def partition(self, sep):
		# type: (Union[str, CIS], ) -> Tuple

		pos = self.find(sep)
		if pos == -1:
			return (self, CaseInsensitiveString(""), CaseInsensitiveString("")) # self should be immutable, make copy?
		else:
			return (self[0:pos], sep, self[pos+len(sep):]) # CaseInsensitiveString(sep) ?

	def replace(self, old, new, count=-1):
		# type: (str, str, int) -> CIS


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

	def rfind(self, sub, start=None, end=None):
		# type: (Union[str, CIS], ) -> int

		return self._s.lower().rfind(sub.lower(), start, end) # isinstance separation?

	def rindex(self, sub, start=None, end=None):
		# type: (Union[str, CIS], ) -> int

		return self._s.lower().rindex(sub.lower(), start, end) # isinstance separation?

	def rjust(self, width, fillchar=" "):
		# type: (int, str) -> CIS

		return CaseInsensitiveString(self._s.rjust(width, fillchar))

	def rpartition(self, sep):
		# type: (Union[str, CIS], ) -> Tuple

		pos = self.rfind(sep)
		if pos == -1:
			return (CaseInsensitiveString(""), CaseInsensitiveString(""), self) # self should be immutable
		else:
			return (self[0:pos], sep, self[pos+len(sep):])

	def rsplit(self, sep=None, maxsplit=-1):
		# type: (Union[str, CIS], int) -> CIS

		if sep is None:
			return list(CaseInsensitiveString(s) for s in self._s.rsplit(sep, maxsplit))
		else:
			raise NotImplementedError

	def rstrip(self, chars=None):
		if chars is None:
			return CaseInsensitiveString(self._s.rstrip()) # only strips case insensitive whitespace anyway

		if isinstance(chars, CaseInsensitiveString):
			cs = set(chars)
		else:
			cs = set(c.lower() for c in chars)

		i = len(self)
		for c in reversed(self):
			if c in cs:
				i -= 1
			else:
				break

		return self._s[:i]

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

	def splitlines(self, keepends=False):
		# type: (bool, ) -> list
		return list(CaseInsensitiveString(line) for line in self._s.splitlines(keepends))

	def startswith(self, prefix, start=None, end=None):
		# type: (Union[str, CIS], ) -> bool

		if isinstance(prefix, CaseInsensitiveString):
			return self._s.lower().startswith(prefix._s.lower(), start, end)
		else:
			return self._s.lower().startswith(prefix.lower(), start, end)

	def strip(self, chars=None):
		if chars is None:
			return CaseInsensitiveString(self._s.strip()) # strip case insensitive whitespace
		else:
			if isinstance(chars, CaseInsensitiveString):
				chars = str(chars)

			chars = "".join(set(chars.lower()) | set(chars.upper()))
			return CaseInsensitiveString(self._s.strip(chars))

	def swapcase(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.swapcase())

	def title(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.title())

	def translate(self, table):
		return CaseInsensitiveString(self._s.translate(table))

	def upper(self):
		# type: () -> CIS

		return CaseInsensitiveString(self._s.upper())

	def zfill(self, width):
		# type: (int, ) -> CIS

		return CaseInsensitiveString(self._s.zfill(width))

class StringEx(CaseInsensitiveString):

	def replace_list(self, character_list, replace_char):
		for find_char in character_list:
			string = self.replace(find_char, replace_char)
		return string

CIS = CaseInsensitiveString

from ferutility.test import MyTestCase, parametrize
class CaseInsensitiveStringTest(MyTestCase):

	@parametrize(
		("a", "a"),
		("a", "A"),
		("A", "a"),
		("Asd", "asD"),
		("asd", "ASD"),
	)
	def test_equal(self, a, b):
		self.assertEqual(CIS(a), CIS(b))

	@parametrize(
		("a", "b"),
		("a", "as")
	)
	def test_equal_not(self, a, b):
		self.assertNotEqual(CIS(a), CIS(b))

	@parametrize(
		("a", "A"),
		("A", "a"),
		("Asd", "asD"),
		("asd", "ASD"),
	)
	def test_hash(self, a, b):
		self.assertEqual(hash(CIS(a)), hash(CIS(b)))

	@parametrize(
		("a", "b"),
		("a", "as")
	)
	def test_hash_not(self, a, b):
		self.assertNotEqual(hash(CIS(a)), hash(CIS(b)))

	@parametrize(
		("asd", "d"),
		("asd", "sd"),
		("asd", "asd"),
		("ASD", "d"),
		("ASD", "sd"),
		("ASD", "asd")
	)
	def test_endswith(self, s, fix):
		self.assertTrue(CIS(s).endswith(CIS(fix)))

	@parametrize(
		("asd", "a"),
		("ASD", "a"),
		("asd", "A"),
		("ASD", "A")
	)
	def test_endswith_not(self, s, fix):
		self.assertFalse(CIS(s).endswith(CIS(fix)))

	@parametrize(
		("A", ),
		("a", ),
		("aA", ),
	)
	def test_lower_upper(self, s):
		self.assertEqual(s.lower(), str(CIS(s).lower()))
		self.assertEqual(s.upper(), str(CIS(s).upper()))

	@parametrize(
		("", "", "", ""),
		("", "asd", "", ""),
		("", "asd", "qwe", ""),
		("asd", "", "", "asd"),
		("asd", "asd", "", ""),
		("", "", "X", "X"),
		("asd", "", "X", "XaXsXd"),
		("asdFGHjkl", "fgh", "123", "asd123jkl"),
		("aaAA", "a", "b", "bbbb"),
		("aaAA", "a", "b", "bbbb"),
	)
	def test_replace(self, s, target, replace, truth):
		result = str(CIS(s).replace(target, replace))
		self.assertEqual(truth, result)

	@parametrize(
		("aaAA", "a", "b", 2, "bbAA"),
		("-aa+aaaa+aa-", "aa", "a", 2, "-a+aaa+aa-"),
	)
	def test_replace_count(self, s, target, replace, count, truth):
		result = str(CIS(s).replace(target, replace, count))
		self.assertEqual(truth, result)

	@parametrize(
		("asd", "a"),
		("asd", "as"),
		("asd", "asd"),
		("ASD", "a"),
		("ASD", "as"),
		("ASD", "asd")
	)
	def test_startswith(self, s, fix):
		self.assertTrue(CIS(s).startswith(CIS(fix)))

	@parametrize(
		("asd", "d"),
		("ASD", "d"),
		("asd", "D"),
		("ASD", "D")
	)
	def test_startswith_not(self, s, fix):
		self.assertFalse(CIS(s).startswith(CIS(fix)))

	@parametrize(
		("asd", "a", "sd"),
		("asd", "d", "as"),
		("asd", "ad", "s"),
		("ASD", "a", "SD"),
		("ASD", "d", "AS"),
		("ASD", "ad", "S"),
	)
	def test_strip(self, s, fix, truth):
		result = str(CIS(s).strip(CIS(fix)))
		self.assertEqual(truth, result)

	@parametrize(
		("asd", "a", "sd"),
		("asd", "d", "asd"),
		("asd", "ad", "sd"),
		("ASD", "a", "SD"),
		("ASD", "d", "ASD"),
		("ASD", "ad", "SD"),
	)
	def test_lstrip(self, s, fix, truth):
		result = str(CIS(s).lstrip(CIS(fix)))
		self.assertEqual(truth, result)

	@parametrize(
		("asd", "a", "asd"),
		("asd", "d", "as"),
		("asd", "ad", "as"),
		("ASD", "a", "ASD"),
		("ASD", "d", "AS"),
		("ASD", "ad", "AS"),
	)
	def test_rstrip(self, s, fix, truth):
		result = str(CIS(s).rstrip(CIS(fix)))
		self.assertEqual(truth, result)

if __name__ == "__main__":
	import unittest
	unittest.main()
