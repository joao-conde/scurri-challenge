import unittest

from postcodes import PostcodeUK

from . import mixins

class PostcodeUKTest(
    unittest.TestCase,
    mixins.TestUtilsMixin
):
    def test_is_valid(self):
        is_valid = PostcodeUK.is_valid("L 1 8 J Q")
        self.assertFalse(is_valid)

        is_valid = PostcodeUK.is_valid("L1 8JQ")
        self.assertTrue(is_valid)

        is_valid = PostcodeUK.is_valid("PO16 7GZ")
        self.assertTrue(is_valid)

        is_valid = PostcodeUK.is_valid("GU16 7HF")
        self.assertTrue(is_valid)

        is_valid = PostcodeUK.is_valid("ASCN 1ZZ")
        self.assertTrue(is_valid)

        is_valid = PostcodeUK.is_valid("BBND 1ZZ")
        self.assertTrue(is_valid)

        is_valid = PostcodeUK.is_valid("SIQQ 1ZZ")
        self.assertTrue(is_valid)

    def test_format(self):
        code = PostcodeUK.format("L1 8JQ")
        self.assertEqual(code, "L1 8JQ")

        code = PostcodeUK.format("BBND1ZZ")
        self.assertEqual(code, "BBND 1ZZ")

        code = PostcodeUK.format("G U1   6 7H   F")
        self.assertEqual(code, "GU16 7HF")

        code = PostcodeUK.format("B BN D1ZZ")
        self.assertEqual(code, "BBND 1ZZ")

        code = PostcodeUK.format("S IQQ 1 ZZ")
        self.assertEqual(code, "SIQQ 1ZZ")

    def test_init(self):
        self.assertNotRaises(ValueError, lambda: PostcodeUK("L 1 8 J Q"))
        self.assertNotRaises(ValueError, lambda: PostcodeUK("L1 8JQ"))

    def test_str(self):
        display = PostcodeUK("L1 8JQ").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'L1 8JQ', 'outward': 'L1', 'inward': '8JQ', 'area': 'L', 'district': '1', 'sector': '8', 'unit': 'JQ'})")

        display = PostcodeUK("PO16 7GZ").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'PO16 7GZ', 'outward': 'PO16', 'inward': '7GZ', 'area': 'PO', 'district': '16', 'sector': '7', 'unit': 'GZ'})")

        display = PostcodeUK("GU16 7HF").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'GU16 7HF', 'outward': 'GU16', 'inward': '7HF', 'area': 'GU', 'district': '16', 'sector': '7', 'unit': 'HF'})")

        display = PostcodeUK("ASCN 1ZZ").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'ASCN 1ZZ', 'outward': 'ASCN', 'inward': '1ZZ'})")

        display = PostcodeUK("BBND 1ZZ").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'BBND 1ZZ', 'outward': 'BBND', 'inward': '1ZZ'})")

        display = PostcodeUK("SIQQ 1ZZ").__str__()
        self.assertEqual(display, "PostcodeUK({'code': 'SIQQ 1ZZ', 'outward': 'SIQQ', 'inward': '1ZZ'})")
