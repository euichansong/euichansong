
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for i in range(N):
        for j in range(M):
            s = arr[i][j]

            for k in range(4):
                for p in range(1, arr[i][j] + 1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]

            if max_val < s:
                max_val = s

    print(max_val)