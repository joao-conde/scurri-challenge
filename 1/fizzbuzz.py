for i in range(1, 101):
    mul_three = i % 3 == 0
    mul_five = i % 5 == 0
    message = str(i) if not mul_three and not mul_five else ""
    message += "Three" if mul_three else ""
    message += "Five" if mul_five else ""
    print(message)
