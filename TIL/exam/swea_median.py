# sort 안쓰고 정렬 len 안쓰고 길이 중간 구하기
scores = [85,72, 38, 80, 69, 65, 68, 96, 22]

def lenlen(scores):
    count = 0
    for i in scores:
        count += 1
    return int(count)
len = lenlen(scores)    

def sorting(scores): # 내림차순 정렬
    scores = [85,72, 38, 69, 80, 65, 68, 96, 22]
    sortlist = [0]
    n = 0
    while scores:
        for i in range(lenlen(scores)):
            if sortlist[n] < scores[i]:
                sortlist[n] = scores[i]
        scores.remove(sortlist[n])
        if scores == []:
            break
        n += 1
        sortlist.append(0)
    return sortlist

def median(scores):
    n = (lenlen(scores)//2)
    return scores[n] 


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
     
    # print(sorting(scores))
    print(median(sorting(scores))) #69
  
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    