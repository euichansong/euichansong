t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr =[[0]*10 for _ in range(10)]
   # print(arr)
    count = 0
    for q in range(n):
        a,b,c,d,e = map(int, input().split())
        for i in range(a,c+1):
            for j in range(b,d+1):
                arr[i][j] += e

    for l in range(10):
        for k in range(10):
            if arr[l][k] == 3:
                count += 1
    print(f'#{tc} {count}')
