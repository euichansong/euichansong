import sys
sys.stdin = open("1215.txt", "r")

t = 10

for tc in range(1,t+1):
    n = int(input())
    mat = [list(input()) for _ in range(8)]
    cnt = 0
    # print(mat)
    # 8*8 배열
    for i in range(8):
        # 최대값 8 넘지 않게
        for j in range(8-n+1):
            # 반으로 나눠서
            # 행 순회
            for k in range(n//2):
                # 첫값과 마지막값이 같으면 회문 아니면 break
                # 0 +0 0+1 0+2, j+n-1-0 j+n-1-2
                if mat[i][j+k] != mat[i][j+n-1-k]:
                    break
            else:
                # 회문이면 +1
                cnt += 1
            # 열 순회
            for k in range(n//2):
                # 0 +0 0+1 0+2, j+n-1-0 j+n-1-2
                # 행 순회에서 ij값 뒤바꿈
                if mat[j+k][i] != mat[j+n-1-k][i]:
                    break
            else:
                cnt += 1
    print(f'#{tc} {cnt}')