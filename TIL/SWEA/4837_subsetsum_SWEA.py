import sys
sys.stdin = open("4837.txt", "r")
t = int(input())


for tc in range(1, t+1):
    arr = [i for i in range(1,13)]

    count = 0
    n, k = map(int, input().split())

    for i in range(1 << 12):  # 부분집합의 개수(1<<n)
        setlist = []
        sum1 = 0
        for j in range(12):
            if i & (1 << j):
                setlist.append(arr[j])
                sum1 += arr[j]
        if len(setlist) == n and sum1 == k:
            count += 1
    print(f'#{tc} {count}')

