from postcodes import Country, Postcode

code = "L1 8JQ"
example = dict(
    code = code,
    is_valid = Postcode.is_valid(Country.UNITED_KINGDOM, code)
)
print(example)

code = "L  1 8  J  Q"
example = dict(
    code = code,
    is_valid = Postcode.is_valid(Country.UNITED_KINGDOM, code)
)
print(example)
