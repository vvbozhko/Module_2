def get_multiplied_digits(number):
    if number % 10 == 0:
        str_number = str(int(number / 10))
    else:
        str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return(first * get_multiplied_digits(int(str_number[1:])))

result1 = get_multiplied_digits(40203)
print(result1)

result2 = get_multiplied_digits(402030)
print(result2)