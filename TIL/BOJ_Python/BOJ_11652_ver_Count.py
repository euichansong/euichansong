# import sys
# from collections import Counter
# a = int(sys.stdin.readline())
# nlist = [] # 입력받은 정수
# vallist = [] # 가장 많이 가지고 있는 정수 리스트
# for i in range(a) :
#     num = int(sys.stdin.readline())
#     nlist.append(num)
# cou = dict(Counter(nlist))
# #.most_common()

# for key, value in cou.items():
#     if max(cou.values()) == value:
#         vallist.append(int(key))
# print(min(vallist))

import sys
from collections import Counter
a = int(sys.stdin.readline())
nlist = [] # 입력받은 정수
vallist = [] # 가장 많이 가지고 있는 정수 리스트
for i in range(a) :
    num = int(sys.stdin.readline())
    nlist.append(num)
cou = dict(Counter(nlist))
#.most_common()
mmax=max(cou.values())############# 시간에 매우 중요
for key, value in cou.items():
    if  value == mmax:
        vallist.append(int(key))
print(min(vallist))
