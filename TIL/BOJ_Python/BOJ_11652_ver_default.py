import sys
a = int(sys.stdin.readline())
nlist = [] # 입력받은 정수
vallist = [] # 가장 많이 가지고 있는 정수 리스트
cou = {}

for i in range(a) :
    num = int(sys.stdin.readline())
    cou.setdefault(num, 0)
    cou[num] += 1

mmax=max(cou.values())

for key, value in cou.items():
    if value == mmax  :
        vallist.append(int(key))
print(min(vallist))