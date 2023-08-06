t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    matrix =[]
    max_v = 0
    for q in range(n):
        arr = list(map(int, input().split()))
        matrix.append(arr)
    # print(matrix)

    for i in range(n):
        for j in range(m):
            sum1 = matrix[i][j]
            for k in range(4):
                for p in range(1, matrix[i][j]+1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < n and 0 <= nj < m:
                        sum1 += matrix[ni][nj]
                    # print(sum1)
            if max_v < sum1:
                max_v = sum1
    print(f'#{tc} {max_v}')



