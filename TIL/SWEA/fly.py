t = int(input())

for tc in range(1, t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    #print(arr)

    max_v = 0

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(i,i+m):
                for p in range(j, j+m):

                    if 0 <= k < n and 0 <= p < n:
                        s += arr[k][p]
            if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')
