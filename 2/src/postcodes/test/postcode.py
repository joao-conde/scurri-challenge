import unittest

from postcodes import Country, Postcode

from . import mixins

class PostcodeTest(
    unittest.TestCase,
    mixins.TestUtilsMixin
):
    def test_build(self):
        self.assertNotRaises(
            ValueError,
            lambda: Postcode.build(Country.UNITED_KINGDOM, "L 1 8 J Q")
        )
        self.assertNotRaises(
            ValueError,
            lambda: Postcode.build(Country.UNITED_KINGDOM, "L1 8JQ")
        )
