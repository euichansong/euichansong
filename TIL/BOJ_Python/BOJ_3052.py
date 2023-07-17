num_list =[]
for i in range(10):
    num = int(input())
    remain = num % 42
    num_list.append(remain)
s = set(num_list)
print(len(s))