# SWEA 알고리즘 하 홀수만 더하기
# 홀수만 더한 값을 출력하는 프로그램
def evenplus(elist):
    res = []
    for i in elist:
        if i % 2 == 1:
            res.append(i)
    res2 = 0
    for k in res:
        res2 += k
    return res2

    pass

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70,35,65,95,75] 
    print(evenplus(scores)) # 270
    
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    