import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    maxv = arr[0]
    minv = arr[0]
    for i in range(n):
        if maxv < arr[i]:
            maxv = arr[i]
        if minv > arr[i]:
            minv = arr[i]
    res = maxv - minv
    print(f'#{test_case} {res}')