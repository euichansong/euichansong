import sys
sys.stdin = open("4861.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]
    cnt = 0
    res = []
    # matrix 전치 행렬
    matrixji = []
    # n*n 행렬
    for i in range(n):
        # n보다 크지 않게
        for j in range(n-m+1):
            # for p in range(j, j+m):
            #     matrix
            # for q in range(j,j+m):
            # 행 검사 반 나눠서 앞뒤로 똑같으면 회문
            for k in range(m//2):
                # j+0, j+1,...j+k  // j+m-1-1, j+m-1-2,...j+m-1-k
                if matrix[i][j+k] != matrix[i][j+m-1-k]:
                    break
            else:
                res.append(''.join(matrix[i][j:j+m]))
            # 열 검사
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        matrixji.append(row)

    for i in range(n):
        for j in range(n-m+1):
            for k in range(m // 2):
                if matrixji[i][j+k] != matrixji[i][j+m-1-k]:
                    break
            else:
                res.append(''.join(matrixji[i][j:j+m]))
    result = ''.join(res)
    print(f'#{tc} {result}')

