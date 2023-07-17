stu_list = [i for i in range(1,31)]
for k in range(28):
    stu = int(input())
    stu_list.remove(stu)

print(min(stu_list))
print(max(stu_list))