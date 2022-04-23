import re

from .interface import PostcodeI

POSTCODE_REGEX_VALUE = "^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
POSTCODE_REGEX = re.compile(POSTCODE_REGEX_VALUE)

SPECIAL_POSTCODE_REGEX_VALUE = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
SPECIAL_POSTCODE_REGEX = re.compile(SPECIAL_POSTCODE_REGEX_VALUE)

class PostcodeUK(PostcodeI):

    @classmethod
    def is_valid(cls, code: str, format: bool = False):
        if format: code = cls.format(code)
        return cls.is_regular(code) or cls.is_special(code)

    @classmethod
    def format(cls, code: str):
        # remove all unecessary white space and add mandatory
        # white space before three last characters
        code = code.replace(" ", "")
        code = code[:-3] + " " + code[-3:]
        return code

    @classmethod
    def is_regular(cls, code: str):
        return POSTCODE_REGEX.match(code) != None

    @classmethod
    def is_special(cls, code: str):
        return not cls.is_regular(code) and SPECIAL_POSTCODE_REGEX.match(code) != None

    def __init__(self, code: str):
        cls = self.__class__

        # formats the postal code
        code = cls.format(code)

        # if validation was requested and this code is not a valid
        # UK postal code, raise a value error
        if not cls.is_valid(code):
            raise ValueError("Invalid UK postal code '%s'" % code)

        self.code = code
        self.outward, self.inward = self.code.split(" ", 1)
        if cls.is_regular(code):
            self.area = self.outward[:2] if self.outward[1].isalpha() else self.outward[0]
            self.district = self.outward[2:] if self.outward[1].isalpha() else self.outward[1:]
            self.sector = self.inward[0]
            self.unit = self.inward[1:]

    def __str__(self):
        return "PostcodeUK(" + str(vars(self)) + ")"
