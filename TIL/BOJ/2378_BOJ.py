# n , m = map(int,input())
# alist = []
# for i in range(n):
#     for k in range(m):
#         aa = list(map(int,input().split()))
#         alist.append([i][k])
#     print(aa)

n , m = map(int,input().split())
alist = []
blist = []
for i in range(n):
    aa = list(map(int, input().split()))
    alist.append(aa)

for k in range(m):
    bb = list(map(int,input().split()))
    blist.append(bb)

for j in range(n):
    for l in range(m):
        print(alist[j][l] + blist[j][l], end = ' ')
    print()