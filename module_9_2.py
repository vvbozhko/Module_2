first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]

second_result = [(fs, ss) for fs in first_strings for ss in second_strings if len(fs) == len(ss)]

third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)