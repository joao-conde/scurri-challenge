import re

from .interface import PostcodeI

POSTCODE_REGEX_VALUE = "^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
""" Regex expression that matches only regular UK postcodes """

SPECIAL_POSTCODE_REGEX_VALUE = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
""" Regex expression that matches all valid UK postcodes (both regular and special ones) """

POSTCODE_REGEX = re.compile(POSTCODE_REGEX_VALUE)

SPECIAL_POSTCODE_REGEX = re.compile(SPECIAL_POSTCODE_REGEX_VALUE)

class PostcodeUK(PostcodeI):
    """
    United Kingdom postcode model and set of utilities.
    """

    @classmethod
    def is_valid(cls, code: str) -> bool:
        return cls.is_regular(code) or cls.is_special(code)

    @classmethod
    def is_regular(cls, code: str) -> bool:
        return POSTCODE_REGEX.match(code) != None

    @classmethod
    def is_special(cls, code: str) -> bool:
        return not cls.is_regular(code) and SPECIAL_POSTCODE_REGEX.match(code) != None

    @classmethod
    def format(cls, code: str) -> str:
        # remove all unecessary white space and add mandatory
        # white space before three last characters
        code = code.replace(" ", "")
        code = code[:-3] + " " + code[-3:]
        return code

    @classmethod
    def resolve_parts(cls, code: str) -> dict:
        parts = dict()
        parts["code"] = code
        parts["outward"], parts["inward"] = code.split(" ", 1)
        if cls.is_regular(code):
            parts["area"] = parts["outward"][:2] if parts["outward"][1].isalpha() else parts["outward"][0]
            parts["district"] = parts["outward"][2:] if parts["outward"][1].isalpha() else parts["outward"][1:]
            parts["sector"] = parts["inward"][0]
            parts["unit"] = parts["inward"][1:]
        return parts

    def __init__(self, code: str):
        cls = self.__class__

        # formats the postal code
        code = cls.format(code)

        # if this code is not a valid UK postal code, raise an error
        if not cls.is_valid(code):
            raise ValueError("Invalid UK postal code '%s'" % code)

        # assign resolved parts to current instance
        parts = cls.resolve_parts(code)
        for part in parts: setattr(self, part, parts[part])

    def __str__(self) -> str:
        return "PostcodeUK(" + str(vars(self)) + ")"
