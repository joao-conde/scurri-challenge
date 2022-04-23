import unittest

from postcode import Country, Postcode

from . import mixins

class PostcodeTest(
    unittest.TestCase,
    mixins.TestUtilsMixin
):
    def test_build(self):
        Postcode.build(Country.UNITED_KINGDOM)
