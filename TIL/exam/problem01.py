# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    res = 1000000000
    for i in scores:
        if res > i:
            res = i
    return res

def max_score(scores):
    res = 0
    for i in scores:
        if res < i:
            res = i
    return res

    pass
    # 여기에 코드를 작성합니다.

def sum_score(scores):
    res = 0
    for i in scores:
        res += i
    return res

def len_score(scores):
    count = 0
    for i in scores:
        count += 1
    return count 


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    print(max_score(scores))
    print(sum_score(scores))
    print(len_score(scores))
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
