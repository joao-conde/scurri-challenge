from enum import Enum

from .postcode_uk import PostcodeUK

class Country(Enum):
    UNITED_KINGDOM = "united_kingdom"

class Postcode:

    BUILDERS = {
        Country.UNITED_KINGDOM: PostcodeUK
    }

    @classmethod
    def build(cls, country: Country, *args, **kwargs):
        if country not in cls.BUILDERS: return None
        return cls.BUILDERS[country](args, kwargs)
