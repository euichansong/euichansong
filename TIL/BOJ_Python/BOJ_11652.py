import sys
from collections import Counter
a = int(sys.stdin.readline())
nlist = [] # 입력받은 정수
vallist = [] # 가장 많이 가지고 있는 정수 리스트
for i in range(a) :
    num = int(sys.stdin.readline())
    nlist.append(num)

cou = dict(Counter(nlist))

# print(cou) #{1: 3, 2: 3}

# 최빈값 구하는 리스트 생성
# for key, value in cou.items():
#     if max(cou.values()) == value:
#         vallist.append(key)
print(cou)
# for key, value in cou.items():
#     if max(cou.values()) == value:
#         print(min(cou.keys()))
#         if min(cou.keys()) == key :
#             #print(key)
#             vallist.append(int(key))
# print(vallist)
for key, value in cou.items():
    if max(cou.values()) == value:
        vallist.append(int(key))
print(min(vallist))

"""
6
-3
-2
-1
0
0
1
[] ?
"""

