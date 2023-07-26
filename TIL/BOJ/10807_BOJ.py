import sys
a = int(input())
b = list(map(int,sys.stdin.readline().split()))
c = int(input())
count = b.count(c)    # 개수 세기
print(count)