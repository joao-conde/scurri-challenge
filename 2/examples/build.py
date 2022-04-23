from postcodes import Postcode, Country

postcode = Postcode.build(Country.UNITED_KINGDOM, "L1 8JQ")
print(postcode)

postcode = Postcode.build(Country.UNITED_KINGDOM, "BBND 1ZZ")
print(postcode)
