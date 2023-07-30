# 이름 min으로 쓰지 말고 더 붙히기
# 최소값 구할땐 엄청 큰 값 초기값으로 넣기
# 최대값 구할땐 엄청 작은 값 초기값으로 넣기
# 만약 범위가 주어진다면 범위보다 작은것, 큰것 넣기
# 길이 구할때 res = 0 그게 최소값이니까
# 결과를 담을 변수는 for문 밖에 있어야 한다
# 만약 시간이 없으면 그냥 min 이렇게 쓰고 반이라도 맞으면 된다.
# min/ max sort[0]/ sort[-1] 로 쓰면 일단은 안된다
def min_score(nums):
    res = 1e9   # 1억
    for n in nums:
        if res > n:
            res = n
    return res


def max_score(nums):
    res = 0
    for n in nums:
        if res <  n:
            res = n
    return res


def len_score(nums):
    res = 0 
    for _ in nums: # for 문에서 빼오긴 할꺼지만 쓰진 않겠다 
        res += 1
    return res


def sum_score(nums):
    res = 0
    for n in nums:
        res += n
    return res


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    print(max_score(scores))
    print(len_score(scores))
    print(sum_score(scores))

    # 아래 부터 추가 예제 코드 작성 가능합니다.


# problem02.py 푼거
def under_60(scores):
    count = 0
    for i in scores:
        if i < 60:
            count += 1
    return count
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# problem03.py 푼거

def is_user_data_valid(user_data):
    if user_data['id'] =='' or user_data['password'] =='' :
        return False
    else:
        return True
    
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# problem04.py 푼거
def is_id_valid(user_data):
    data = ['0','1','2','3','4','5','6','7','8','9']
    print(type(user_data['id'][-1]))  # str
    if user_data['id'][-1] in data:
        return True
    else:
        return False
    
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
    # 아래 부터 추가 예제 코드 작성 가능합니다.