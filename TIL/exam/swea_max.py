# SWEA 알고리즘 하 최대수 구하기
def max_list(scores):
    res = 0
    for i in scores:
        if res < i :
            res = i
    return res
    pass




if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [22, 8, 5, 123, 7, 2, 63, 7, 3, 46]
    print(max_list(scores))
    # print(min_score(scores)) # 30
    # print(max_score(scores))
    # print(sum_score(scores))
    # print(len_score(scores))
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    