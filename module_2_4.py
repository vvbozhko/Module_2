numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
#is_prime = True
for i in range(2, len(numbers)+1):
    is_prime = True
    for j in range(2, len(numbers)):
        if i != j and i % j == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == 1:
        primes.append( i )
    else:
        not_primes.append( i )
print(f'Исходный код:')
print (f'numbers= {numbers}')
print(f'Вывод на консоль:')
print (f'Primes: {primes}')
print (f'Not Primes: {not_primes}')
