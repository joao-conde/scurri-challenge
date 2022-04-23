from postcodes import Country, Postcode

code = "L 1 8J  Q"
example = dict(
    code = code,
    is_valid = Postcode.is_valid(Country.UNITED_KINGDOM, code)
)
print(example)

formatted = Postcode.format(Country.UNITED_KINGDOM, code)
example = dict(
    formatted = formatted,
    is_valid = Postcode.is_valid(Country.UNITED_KINGDOM, formatted)
)
print(example)
