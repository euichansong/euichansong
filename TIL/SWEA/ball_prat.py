t = int(input())
for tc in range(1, t+1):
    n , m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    max_v = 0
    for i in range(n):
        for j in range(m):
            sum1 = arr[i][j]
            for p in range(4):
                for k in range(1, arr[i][j]+1):
                    ni = i + di[p] * k
                    nj = j + dj[p] * k
                    if 0 <= ni < n and 0 <= nj < m:
                        sum1 += arr[ni][nj]
            if max_v < sum1:
                max_v = sum1
    print(f'#{tc} {max_v}')