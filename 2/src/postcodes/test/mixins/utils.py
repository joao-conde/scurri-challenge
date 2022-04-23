class TestUtilsMixin():
    def assertNotRaises(self, error_type, func):
        try:
            func()
        except error_type:
            raise AssertionError("%s not raised by %s" % (error_type, func))
