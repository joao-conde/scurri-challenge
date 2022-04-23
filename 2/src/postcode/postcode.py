from abc import abstractmethod

class Postcode:

    @classmethod
    @abstractmethod
    def is_valid(cls, code: str):
        pass
