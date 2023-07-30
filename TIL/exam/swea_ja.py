# SWEA 알고리즘 하 자릿수 더하기
def ja(s):
    
    if s >= 1000:
        a = s // 1000
        b = (s - (a * 1000)) // 100
        c = (s - (a*1000 + b*100)) // 10
        d = s - (a*1000 + b*100 + c*10) 
        return a+b+c+d
    elif s >= 100:
        a = s // 100
        b = (s - (a * 100)) // 10
        c = s - (a*100 + b*10)
        return a+b+c
    elif s >= 10 :
        a = s // 10
        b = s - (a * 10)
        return a+b
    else:
        return s


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    s = 6789
    print(ja(s))

