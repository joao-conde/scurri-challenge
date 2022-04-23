class PostcodeI:

    @classmethod
    def is_valid(cls, code: str, format: bool = False):
        raise NotImplementedError()

    @classmethod
    def format(cls, code: str):
        raise NotImplementedError()
