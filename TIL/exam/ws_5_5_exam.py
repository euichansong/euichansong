def even_elements(list):
    res = []
    for i in list:
        if i % 2 == 0:
            res.append(i)
    return res

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)