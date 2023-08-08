import sys
sys.stdin = open("9012.txt", "r")
# 받은 입력값
t = int(input())
# 닫는걸 음수로 해야 합이 음수면 break 가능
vps_dict = {'(': 1, ')': -1}
for i in range(t):
    # 받은 배열
    arr = list(input())
    # 총 합
    sum1 = 0
    # 받은 배열의 값에서
    for i in arr:
        # 만약 i가 '(' 라면
        if vps_dict[i] == 1:
            # 만약 총 합이 음수라면(먼저 닫았다면) 반복 종료
            if sum1 < 0:
                break
            else:
                # 총합이 음수가 아니라면 총합에 키값에 따른 밸류 추가
                sum1 += vps_dict[i]
        # 만약 i가 ')' 라면
        elif vps_dict[i] == -1:
            # 만약 총 합이 음수라면(먼저 닫았다면) 반복 종료
            if sum1 < 0:
                break
            else:
                # 총합이 음수가 아니라면 총합에 키값에 따른 밸류 추가
                sum1 += vps_dict[i]
    # 총합이 0이라면(괄호가 다 닫혀있으면)
    if sum1 == 0:
        print("YES")
    else:
        print("NO")

    # for i in range(n-1):
    #     min_v = i
    #
    #     for j in range(i+1,n):
    #         if gns_dict[data[j]] < gns_dict[data[min_v]]:
    #             min_v = j
    #     data[i] , data[min_v] = data[min_v] , data[i]

"""
10을 짝으로 해서  
1100100
1111010010
110100111000
선택정렬로 1 0 1 0 해서 끝이 0이면 예스 아니면 노
"""
