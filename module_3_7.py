[1, 2, 3],
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0


def hard(*args):
    global summa
    for i in range(0, len(args)):
        if isinstance(args[i], dict):
            summ = 0
            for key, values in args[i].items():
                sum_d += (len(key) + values)
            summa += sum_d
        if isinstance(args[i], (list, tuple, set, str)):
            d = list(args[i])
            sum_i = 0
            sum_d = 0
            sum_s = 0
            for j in range(0, len(d)):
                if isinstance(d[j], list):
                    hard(d[j])
                if isinstance(d[j], set):
                    hard(list(d[j]))
                if isinstance(d[j], tuple):
                    # if len(d[j]) == 0:
                    #     summa += 1
                    # else:
                    hard(d[j])
                if isinstance(d[j], int):
                    sum_i += d[j]
                if isinstance(d[j], dict):
                    sum_d = 0
                    for key, values in d[j].items():
                        sum_d += (len(key) + values)
                if isinstance(d[j], str):
                    sum_s += len(d[j])

            summa += sum_i + sum_d + sum_s
    return (summa)

result = hard(data_structure)
print(result)