#a,b,c,d,e = list(input())
# a = list(input())
# b = list(input())
# c = list(input())
# d = list(input())
# e = list(input())
# # for h in range(5):
# for i in range(len(a)):
#     for j in range(len(b)):
#         for k in range(len(c)):
#             for l in range(len(d)):
#                 for m in range(len(e)):
#                     print(a[i]+b[j]+c[k]+d[l]+e[m], end = ' ')
#                         #print(a+b+c+d+e, end = ' ')
# print(max(len(a,b,c,d,e)))
# 첫번째 줄의 0번뽑고 2번째 0번.... 없으면 continue 
# for i in range():
#     print(a[i]+b[i]+c[i]+d[i]+e[i] ,end = '')
# for i in range(len(a)):
#     kj
# if 

alist = [input()for i in range(5)]

for j in range(15):
    for k in range(5): 
        # k가 0일때 aabcdd 를 돈다 j가 0이니까 a 출력 
        # k가 1일때 adzz 를 돈다 j가  0이니까 a 출력
        # j가 4일때 k 1인경우 afzz에서 4< len('afzz') 이기때문에 문자열 출력 안된다
        if j < len(alist[k]):
            print(alist[k][j], end= '')