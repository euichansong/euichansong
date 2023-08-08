import sys
sys.stdin = open("3143.txt", "r")

# 입력값
t = int(input())
# 테스트 케이스
for tc in range(1, t+1):
    # 텍스트 패턴 입력값
    text, pattern = input().split()
    # print(text, pattern)
    # 텍스트 길이
    text_len = len(text)
    # 패턴 길이
    pattern_len = len(pattern)
    # 초기화
    i = 0
    j = 0
    cnt = 0
    # i가 텍스트 길이보다 작고 j가 패턴 길이보다 작을때 까지
    while i < text_len and j < pattern_len:
        # 만약 텍스트와 패턴이 다른 경우
        if text[i] != pattern[j]:
            # 텍스트 인덱스를 j만큼 되돌린다
            i = i - j
            # 패턴 인덱스 초기화
            j = -1
        # 증가
        i += 1
        j += 1
        # 패턴 인덱스가 패턴 길이와 같으면
        if j == pattern_len:
            # 카운팅
            cnt += 1
            # j값 초기화
            j = 0
    # print(cnt)
    # 타이핑 횟수 = 텍스트 길이 - 패턴길이*카운트 횟수 + 카운트
    # 패턴길이 * 카운트 횟수는 텍스트에서 겹친 패턴만큼 빼주고
    # 카운트가 타이핑이기 떄문에 더해준다
    print(f'#{tc} {text_len - (pattern_len*cnt) + cnt}')
