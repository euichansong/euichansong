import sys
num = int(sys.stdin.readline())
new_dict = {}

for i in range(num):
    key_num = sys.stdin.readline()
    new_dict.setdefault(key_num, 0)
    new_dict[key_num] += 1

max_values = max((new_dict).values())

new_lst = []
for key, value in new_dict.items():
    if value == max_values:
        new_lst.append(int(key))
print(min(new_lst))