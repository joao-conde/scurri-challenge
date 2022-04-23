import unittest

import postcode

from .utils import TestUtilsMixin

class PostcodeUKTest(
    unittest.TestCase,
    TestUtilsMixin
):
    def test_is_valid(self):
        is_valid = postcode.PostcodeUK.is_valid("L 1 8 J Q")
        self.assertFalse(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("L 1 8 J Q", format = True)
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("L1 8JQ")
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("PO16 7GZ")
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("GU16 7HF")
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("ASCN 1ZZ")
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("BBND 1ZZ")
        self.assertTrue(is_valid)

        is_valid = postcode.PostcodeUK.is_valid("SIQQ 1ZZ")
        self.assertTrue(is_valid)

    def test_init(self):
        self.assertRaises(ValueError, lambda: postcode.PostcodeUK("L 1 8 J Q"))
        self.assertNotRaises(ValueError, lambda: postcode.PostcodeUK("L1 8JQ"))
        self.assertNotRaises(ValueError, lambda: postcode.PostcodeUK("L 1 8 J Q", validate = False))

    def test_format_code(self):
        code = postcode.PostcodeUK.format_code("L1 8JQ")
        self.assertEqual(code, "L1 8JQ")

        code = postcode.PostcodeUK.format_code("BBND1ZZ")
        self.assertEqual(code, "BBND 1ZZ")

        code = postcode.PostcodeUK.format_code("G U1   6 7H   F")
        self.assertEqual(code, "GU16 7HF")

        code = postcode.PostcodeUK.format_code("B BN D1ZZ")
        self.assertEqual(code, "BBND 1ZZ")

        code = postcode.PostcodeUK.format_code("S IQQ 1 ZZ")
        self.assertEqual(code, "SIQQ 1ZZ")
