my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)
index = 0
while index < length:
    if my_list[index] > 0:
        print (my_list[index])
        index = index + 1
    else:
        index = index + 1
