import unittest

from postcode import PostcodeUK

from . import mixins

class PostcodeUKTest(
    unittest.TestCase,
    mixins.TestUtilsMixin
):
    def test_is_valid(self):
        is_valid = PostcodeUK.is_valid("L 1 8 J Q")
        self.assertFalse(is_valid)

        is_valid = PostcodeUK.is_valid("L 1 8 J Q", format = True)
        self.assertTrue(is_valid)

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
        self.assertRaises(ValueError, lambda: PostcodeUK("L 1 8 J Q"))
        self.assertNotRaises(ValueError, lambda: PostcodeUK("L1 8JQ"))
