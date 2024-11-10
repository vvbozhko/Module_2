number1 = input ('Введите первое число ')
number2 = input ('Введите второе число ')
number3 = input ('Введите третье число ')
if number1 == number2:
    if number2 == number3:
        print ('3')
    else:
        print ('2')
elif number1 == number3:
    print ('2')
elif number2 == number3:
    print ('2')
else:
    print ('0')