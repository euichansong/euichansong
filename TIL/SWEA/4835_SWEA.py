# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for tc in range(1, T + 1):
#     n, m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     sortarr = sorted(arr)
#     minlist = []
#     maxlist = []
#     for i in range(m):
#
#         minlist.append(sortarr[i])
#     for k in range(n , n - m , -1):
#
#         maxlist.append(sortarr[k-1])
#     res = sum(maxlist) - sum(minlist)
#     print(f'#{T} {res}')
#
# #1만 성공
# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for tc in range(1, T + 1):
#     n, m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     minx = 0
#     maxx = 10e9
#     for i in range(n-1, 0 , -1):
#         for j in range(i, 1 , -1):
#             if arr[j-2]+arr[j-1]+ arr[j] < maxx:
#                 maxx = arr[j-2] + arr[j - 1] + arr[j]
#             if arr[j-2]+arr[j-1]+ arr[j] > minx:
#                 minx = arr[j-2]+arr[j-1]+ arr[j]
#     res = maxx - minx
#     print(maxx)
#     print(minx)
#     print(f'#{tc} {res}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):

    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    sumlist = []
    for i in range(n-m+1):
        sum = 0
        for j in range(i, i + m):
            sum += arr[j]
        sumlist.append(sum)
    res = max(sumlist) - min(sumlist)
    print(f'#{tc} {res}')


