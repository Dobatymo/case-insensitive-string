from genutility.test import MyTestCase, parametrize

from case_insensitive_string.cis import CIS


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

    @parametrize(("a", "b"), ("a", "as"))
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

    @parametrize(("a", "b"), ("a", "as"))
    def test_hash_not(self, a, b):
        self.assertNotEqual(hash(CIS(a)), hash(CIS(b)))

    @parametrize(
        ("asd", "d"),
        ("asd", "sd"),
        ("asd", "asd"),
        ("ASD", "d"),
        ("ASD", "sd"),
        ("ASD", "asd"),
    )
    def test_endswith(self, s, fix):
        self.assertTrue(CIS(s).endswith(CIS(fix)))

    @parametrize(("asd", "a"), ("ASD", "a"), ("asd", "A"), ("ASD", "A"))
    def test_endswith_not(self, s, fix):
        self.assertFalse(CIS(s).endswith(CIS(fix)))

    @parametrize(
        ("A",),
        ("a",),
        ("aA",),
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
        ("ASD", "asd"),
    )
    def test_startswith(self, s, fix):
        self.assertTrue(CIS(s).startswith(CIS(fix)))

    @parametrize(("asd", "d"), ("ASD", "d"), ("asd", "D"), ("ASD", "D"))
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
