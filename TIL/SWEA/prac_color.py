t= int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    for q in range(n):
        a,b,c,d,e = map(int,input().split())
        for i in range(a, c+1):
            for j in range(b, d+1):
                arr[i][j] += e

    count = 0
    for k in range(10):
        for l in range(10):
            if arr[k][l] == 3:
                count += 1
    print(f'#{tc} {count}')