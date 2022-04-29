MATCHES = {
    "}": "{",
    ")": "(",
    "]": "["
}

def is_balanced(chars):
    stack = []
    for c in chars:
        if c in MATCHES.values():
            stack.append(c)
        if c in MATCHES.keys():
            if stack[-1] != MATCHES[c]: return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("{}()"))
print(is_balanced("[({})]"))
print(is_balanced("{{{}}}"))
print(is_balanced("{)(}"))
print(is_balanced("{(}"))
print(is_balanced("{()"))
