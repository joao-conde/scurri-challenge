class PostcodeI:
    """
    Postcode base interface that every country implementation
    should extend and implement.
    """

    @classmethod
    def is_valid(cls, code: str) -> bool:
        raise NotImplementedError()

    @classmethod
    def format(cls, code: str) -> str:
        raise NotImplementedError()
