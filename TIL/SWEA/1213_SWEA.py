import sys
sys.stdin = open("1213.txt", "r", encoding= 'UTF8')

def BruteForce(p,t):
    i = 0
    j = 0
    cnt = 0
    while j < M and i < N:

        # 텍스트와 패턴이 다른 경우
        if t[i] != p[j]:
            # 텍스트 인덱스를 j만큼 되돌린다
            i = i - j
            # 패턴 인덱스 초기화
            j = -1
        # 증가
        i += 1
        j += 1
        # 패턴 인덱스가 패턴 길이와 같으면
        if j == M:
        # print(M)
        # print(j)
        # cnt += 1
        # 카운트 1 증가
            cnt += 1
        # j = -1 을 하면 안된다 위의 코드는
        # 바로 1을 증가 시켜주기 때문에 -1이 초기화이다
            j = 0


        # print(cnt)
    return cnt

for _ in range(10):
    tc = input()
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)
    # print(BruteForce(pattern,text))
    # print(BruteForce(pattern, text))
    print(f'#{tc} {BruteForce(pattern, text)}')