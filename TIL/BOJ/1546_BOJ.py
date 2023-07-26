sub = int(input())

sub_list = []
all_test = list(map(int,input().split()))
aver = max(all_test)
print(all_test)
print(aver)
for k in range(len(all_test)):
    a = all_test[k] / aver*100
    sub_list.append(a)
print(sub_list)
result1 = sum(sub_list) / len(sub_list)
result = format(result1,".2f")
print(result)