import re

from .postcode import Postcode

POSTCODE_REGEX_VALUE = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

POSTCODE_REGEX = re.compile(POSTCODE_REGEX_VALUE)

class PostcodeUK(Postcode):
    def __init__(self, code):
        # if this code is not a valid UK
        # postal code, raise an error
        cls = self.__class__
        if not cls.is_valid(code):
            raise ValueError("Invalid UK postal code format")
        
        self.area = ""
        self.district = "" 

    @classmethod
    def is_valid(cls, code: str):
        return POSTCODE_REGEX.match(code) != None