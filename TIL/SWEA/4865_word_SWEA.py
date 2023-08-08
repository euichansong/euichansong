import sys
sys.stdin = open("4865.txt", "r") # , encoding= 'UTF8'
#
t = int(input())

for tc in range(1, t+1):
    # 패턴 입력값 리스트
    strp = list(input())
    # 텍스트 입력값 리스트
    strt = list(input())
    # print(str1) # ['X', 'Y', 'P', 'V']
    # 패턴 길이
    m = len(strp)
    # 텍스트 길이
    n = len(strt)
    # 결과값 리스트
    res = []
    max_v = 0
    # 패턴 단어들 범위
    for j in strp:
        i = 0
        cnt = 0
        # 텍스트 길이보다 길지 않게
        while i < n:
            # 패턴과 텍스트가 같으면
            if j == strt[i]:
                #print(strt[i])
                # 카운팅
                cnt += 1
            # i에 1 더해줌
            i += 1
        # 결과값 리스트
        res.append(cnt)
    # 최대값 리스트
    for k in res:
        if max_v < k:
            max_v = k
    # 출력 결과
    print(f'#{tc} {max_v}')




