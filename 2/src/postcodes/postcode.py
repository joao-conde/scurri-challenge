from enum import Enum

from .interface import PostcodeI
from .postcode_uk import PostcodeUK

class Country(Enum):
    UNITED_KINGDOM = "united_kingdom"

class Postcode:

    BUILDERS = {
        Country.UNITED_KINGDOM: PostcodeUK
    }

    @classmethod
    def build(cls, country: Country, code: str, **kwargs) -> PostcodeI:
        return cls.BUILDERS[country](code, **kwargs)
