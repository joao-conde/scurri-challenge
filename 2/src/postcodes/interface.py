class PostcodeI:

    @classmethod
    def is_valid(cls, code: str, format: bool = False) -> bool:
        raise NotImplementedError()

    @classmethod
    def format(cls, code: str) -> str:
        raise NotImplementedError()
