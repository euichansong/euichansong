# set 안쓰고 교집합 찾기


def set_score(scores1,scores2, scores3):
    res = []
    for i in scores1:
        if i in scores2 and i in scores3:
            res.append(i)
    return res

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores1 = [30, 60, 90, 70]
    scores2 = [80, 60, 90, 50]
    scores3 = [30, 60, 100, 400]
    # print(min_score(scores)) # 30
    # print(max_score(scores))
    # print(sum_score(scores))
    # print(len_score(scores))
    print(set_score(scores1,scores2, scores3))
    # 아래 부터 추가 예제 코드 작성 가능합니다.