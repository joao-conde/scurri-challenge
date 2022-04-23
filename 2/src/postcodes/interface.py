class PostcodeI:

    @classmethod
    def is_valid(cls, code: str) -> bool:
        raise NotImplementedError()

    @classmethod
    def format(cls, code: str) -> str:
        raise NotImplementedError()
