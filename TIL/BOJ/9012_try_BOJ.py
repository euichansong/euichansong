t = int(input())
vps_dict = {'(': 1, ')': 0}
for i in range(t):
    arr = list(input())
    # print(arr)
    newarr = []
    res = []
    cnt1 = 0
    cnt0 = 0
    for i in range(len(arr)):
        newarr.append(vps_dict[arr[i]])
    # #print(newarr)
    # for i in range(len(newarr)-1,0,-1):
    #     for j in range(0,i):
    #         if newarr[j]>newarr[j+1]:
    #             newarr[j], newarr[j + 1] = newarr[j+1], newarr[j]
    # print(newarr)
    for k in newarr:
        if k == 1:
            cnt1 += 1
        if k == 0:
            cnt0 += 0
    if (cnt1 != 0 or cnt0 != 0) and cnt1 == cnt0:
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
여는게 먼저여야 된다
"""
