li = []
num = 0
for i in range(5):
    a = int(input())
    li.append(a)
# print(li) [10, 40, 30, 60, 30]
for i in li:
    num += i
print(int(num/len(li)))

b = sorted(li)
me = len(b)//2
print(int(b[me]))