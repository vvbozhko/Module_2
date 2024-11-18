def get_pas(n):
    pas = []
    for i in range(1, (int(n / 2) + 1)):
        if i < n / 2 or n % i == 0:
            for j in range(2, n):
                if n % (i + j) == 0:
                    pas.append([i] + [j])
    return pas

n = int(input(f'Введите число от 3 до 20 - '))
result = (get_pas(n))
print(*sum(result, []))
