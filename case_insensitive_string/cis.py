from typing import Any, Iterable, Iterator, Mapping, Optional, Tuple, Union

from typing_extensions import Self


class CaseInsensitiveString:
    """Case insensitive string"""

    def __init__(self, s: str) -> None:
        self._s = s

    def __fspath__(self) -> str:
        return self._s

    def __repr__(self) -> str:
        return f"CaseInsensitiveString({repr(self._s)})"

    def __str__(self) -> str:
        return self._s

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() == other._s.lower()
        else:
            return self._s.lower() == other.lower()

    def __ne__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() != other._s.lower()
        else:
            return self._s.lower() != other.lower()

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() < other._s.lower()
        else:
            return self._s.lower() < other.lower()

    def __le__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() <= other._s.lower()
        else:
            return self._s.lower() <= other.lower()

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() > other._s.lower()
        else:
            return self._s.lower() > other.lower()

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return self._s.lower() >= other._s.lower()
        else:
            return self._s.lower() >= other.lower()

    def __add__(self, other: "CIS") -> "CIS":
        if isinstance(other, CaseInsensitiveString):
            return CaseInsensitiveString(self._s + other._s)
        else:
            return CaseInsensitiveString(self._s + other)

    def __mul__(self, other: int) -> "CIS":
        return CaseInsensitiveString(self._s * other)

    def __mod__(self, other: Tuple) -> "CIS":
        return CaseInsensitiveString(self._s % other)

    def __len__(self) -> int:
        return len(self._s)  # the length of the lowercase version might be different

    def __iter__(self) -> Iterator["CIS"]:
        for c in self._s:
            yield CaseInsensitiveString(c)

    def __hash__(self) -> int:
        return hash(self._s.lower())

    def __getitem__(self, key: Union[int, slice]) -> "CIS":
        return CaseInsensitiveString(self._s[key])

    def __contains__(self, other: Union[str, "CIS"]) -> bool:
        if isinstance(other, CaseInsensitiveString):
            return other._s.lower() in self._s.lower()
        else:
            return other.lower() in self._s.lower()

    def capitalize(self) -> "CIS":
        return CaseInsensitiveString(self._s.capitalize())

    def casefold(self) -> "CIS":
        return CaseInsensitiveString(self._s.casefold())

    def center(self, width: int, fillchar: str = " ") -> "CIS":
        return CaseInsensitiveString(self._s.center(width, fillchar))

    def count(
        self,
        sub: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int:
        if isinstance(sub, CaseInsensitiveString):
            return self._s.lower().count(sub._s.lower(), start, end)
        else:
            return self._s.lower().count(sub.lower(), start, end)

    def encode(self, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        return self._s.encode(encoding, errors)

    def endswith(
        self,
        suffix: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> bool:
        if isinstance(suffix, CaseInsensitiveString):
            return self._s.lower().endswith(suffix._s.lower(), start, end)
        else:
            return self._s.lower().endswith(suffix.lower(), start, end)

    def expandtabs(self, tabsize: int = 8) -> "CIS":
        return CaseInsensitiveString(self._s.expandtabs(tabsize))

    def find(
        self,
        sub: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int:
        if isinstance(sub, CaseInsensitiveString):
            return self._s.lower().find(sub._s.lower(), start, end)
        else:
            return self._s.lower().find(sub.lower(), start, end)

    def format(self, *args: Any, **kwargs: Any) -> "CIS":
        return CaseInsensitiveString(self._s.format(*args, **kwargs))

    def format_map(self, mapping: Mapping) -> "CIS":
        return CaseInsensitiveString(self._s.format_map(mapping))

    def index(
        self,
        sub: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int:
        if isinstance(sub, CaseInsensitiveString):
            return self._s.lower().index(sub._s.lower(), start, end)
        else:
            return self._s.lower().index(sub.lower(), start, end)

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

    def join(self, iterable: Iterable) -> "CIS":
        return CaseInsensitiveString(self._s.join(iterable))

    def ljust(self, width: int, fillchar: str = " ") -> "CIS":
        return CaseInsensitiveString(self._s.ljust(width, fillchar))

    def lower(self) -> "CIS":
        return CaseInsensitiveString(self._s.lower())

    def lstrip(self, chars: Optional["CIS"] = None) -> "CIS":
        if chars is None:
            return CaseInsensitiveString(self._s.lstrip())  # only strips case insensitive whitespace anyway

        if isinstance(chars, CaseInsensitiveString):
            cs = set(chars)
        else:
            cs = {c.lower() for c in chars}

        i = 0
        for c in self:
            if c in cs:
                i += 1
            else:
                break

        return self[i:]

    @staticmethod
    def maketrans(x, y=None, z=None) -> dict:  # create case insensitive dict here?
        return str.maketrans(x, y, z)

    def partition(self, sep: Union[str, "CIS"]) -> Tuple:
        pos = self.find(sep)
        if pos == -1:
            return (
                self,
                CaseInsensitiveString(""),
                CaseInsensitiveString(""),
            )  # self should be immutable, make copy?
        else:
            return (
                self[0:pos],
                sep,
                self[pos + len(sep) :],
            )  # CaseInsensitiveString(sep) ?

    def replace(self, old: str, new: str, count: int = -1) -> Self:
        if not old and not new:
            return self

        start = 0
        ret = self._s

        while count != 0:
            if old:
                start = ret.lower().find(old.lower(), start)
            if start >= 0:
                ret = ret[:start] + new + ret[start + len(old) :]
                if not old:
                    start += 1
                    if start + 1 >= len(ret):
                        break

                start += len(new)
                count -= 1
            else:
                break

        return CaseInsensitiveString(ret)

    def rfind(
        self,
        sub: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int:
        return self._s.lower().rfind(sub.lower(), start, end)  # isinstance separation?

    def rindex(
        self,
        sub: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int:
        return self._s.lower().rindex(sub.lower(), start, end)  # isinstance separation?

    def rjust(self, width: int, fillchar: str = " ") -> "CIS":
        return CaseInsensitiveString(self._s.rjust(width, fillchar))

    def rpartition(self, sep: Union[str, "CIS"]) -> Tuple:
        pos = self.rfind(sep)
        if pos == -1:
            return (
                CaseInsensitiveString(""),
                CaseInsensitiveString(""),
                self,
            )  # self should be immutable
        else:
            return (self[0:pos], sep, self[pos + len(sep) :])

    def rsplit(self, sep: Union[str, "CIS"] = None, maxsplit: int = -1) -> "CIS":
        if sep is None:
            return list(CaseInsensitiveString(s) for s in self._s.rsplit(sep, maxsplit))
        else:
            raise NotImplementedError

    def rstrip(self, chars=None):
        if chars is None:
            return CaseInsensitiveString(self._s.rstrip())  # only strips case insensitive whitespace anyway

        if isinstance(chars, CaseInsensitiveString):
            cs = set(chars)
        else:
            cs = {c.lower() for c in chars}

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
                raise TypeError(f"must be str or None, not {type(sep)}")
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

    def splitlines(self, keepends: bool = False) -> list:
        return list(CaseInsensitiveString(line) for line in self._s.splitlines(keepends))

    def startswith(
        self,
        prefix: Union[str, "CIS"],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> bool:
        if isinstance(prefix, CaseInsensitiveString):
            return self._s.lower().startswith(prefix._s.lower(), start, end)
        else:
            return self._s.lower().startswith(prefix.lower(), start, end)

    def strip(self, chars=None):
        if chars is None:
            return CaseInsensitiveString(self._s.strip())  # strip case insensitive whitespace
        else:
            if isinstance(chars, CaseInsensitiveString):
                chars = str(chars)

            chars = "".join(set(chars.lower()) | set(chars.upper()))
            return CaseInsensitiveString(self._s.strip(chars))

    def swapcase(self) -> "CIS":
        return CaseInsensitiveString(self._s.swapcase())

    def title(self) -> "CIS":
        return CaseInsensitiveString(self._s.title())

    def translate(self, table):
        return CaseInsensitiveString(self._s.translate(table))

    def upper(self) -> "CIS":
        return CaseInsensitiveString(self._s.upper())

    def zfill(self, width: int) -> "CIS":
        return CaseInsensitiveString(self._s.zfill(width))


CIS = CaseInsensitiveString
