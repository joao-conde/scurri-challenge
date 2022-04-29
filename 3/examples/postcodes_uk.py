from postcodes import PostcodeUK

code = "L1 8JQ"
example = dict(
    code = code,
    is_valid = PostcodeUK.is_valid(code),
    is_regular = PostcodeUK.is_regular(code),
    is_special = PostcodeUK.is_special(code),
    postcode = str(PostcodeUK(code))
)
print(example)

code = "ASCN 1ZZ"
example = dict(
    code = code,
    is_valid = PostcodeUK.is_valid(code),
    is_regular = PostcodeUK.is_regular(code),
    is_special = PostcodeUK.is_special(code),
    postcode = str(PostcodeUK(code))
)
print(example)
