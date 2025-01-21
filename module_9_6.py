def all_variants(text):
    length = len(text)
    for i in range(0, length):
        for j in range(length - i):
            yield text[j:j + i + 1]

#
a = all_variants("abc")

for i in a:
    print(i)
