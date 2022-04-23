from .postcode_uk import PostcodeUK

class Postcode:

    COUNTRIES = {
        "uk": PostcodeUK
    }

    @classmethod
    def build(cls, country):
        country = country.lower()
        if country not in cls.COUNTRIES: return None
        return cls.COUNTRIES[country]
