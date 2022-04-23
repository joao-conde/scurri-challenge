from enum import Enum

from .interface import PostcodeI
from .postcode_uk import PostcodeUK

class Country(Enum):
    UNITED_KINGDOM = "united_kingdom"

class Postcode(PostcodeI):

    BUILDERS = {
        Country.UNITED_KINGDOM: PostcodeUK
    }

    @classmethod
    def build(cls, country: Country, code: str, **kwargs) -> PostcodeI:
        return cls.BUILDERS[country](code, **kwargs)

    @classmethod
    def is_valid(cls, country: Country, code: str) -> bool:
        return cls.BUILDERS[country].is_valid(code)

    @classmethod
    def format(cls, country: Country, code: str) -> str:
        return cls.BUILDERS[country].format(code)
