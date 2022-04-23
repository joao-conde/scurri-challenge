import unittest

from postcodes import PostcodeI

from . import mixins

class InterfaceTest(
    unittest.TestCase,
    mixins.TestUtilsMixin
):
    def test_is_valid(self):
        self.assertRaises(NotImplementedError, lambda: PostcodeI.is_valid("L1 8JQ"))

    def test_format(self):
        self.assertRaises(NotImplementedError, lambda: PostcodeI.format("BBND1ZZ"))
