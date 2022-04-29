from postcodes import Country, Postcode

code = "L 1 8J  Q"
example = dict(
    code = code,
    formatted = Postcode.format(Country.UNITED_KINGDOM, code)
)
print(example)
