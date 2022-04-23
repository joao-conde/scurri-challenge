import unittest

import postcode

from .utils import TestUtilsMixin

class PostcodeUKTest(
    unittest.TestCase,
    TestUtilsMixin
):
    def test_is_valid(self):
        is_valid = postcode.PostcodeUK.is_valid("123")
        self.assertFalse(is_valid)

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
        self.assertRaises(ValueError, lambda: postcode.PostcodeUK("123"))
        self.assertNotRaises(ValueError, lambda: postcode.PostcodeUK("L1 8JQ"))
