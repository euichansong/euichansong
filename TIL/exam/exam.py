def is_user_data_valid(user_data):
    if user_data['id'] =='' or user_data['password'] =='' :
        return False
    else:
        return True
    
    # 여기에 코드를 작성합니다.
    # a = list(range(1,10))
    # print(map(str,a))

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': '1q2w3e4r',
        'password': '',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2))

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