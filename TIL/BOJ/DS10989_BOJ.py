import sys
n = int(sys.stdin.readline())
al = []
for i in range(n):
    a = int(sys.stdin.readline())
    al.append(a)

al.sort()
for i in al:
    print(i)