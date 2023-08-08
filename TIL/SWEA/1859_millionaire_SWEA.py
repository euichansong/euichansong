import sys
sys.stdin = open("mini1859.txt", "r")

import copy

t =int(input())

for tc in range(1, t+1):
    n = int(input())
    sell = list(map(int, input().split()))
    sortsell = copy.deepcopy(sell) # 내림차순
    sell_len = len(sell)


    for i in range(sell_len -1):
        max_v = i
        for j in range(i+1, sell_len):
            if sortsell[j] > sortsell[max_v]:
                max_v = j
        sortsell[i], sortsell[max_v] = sortsell[max_v], sortsell[i]
    # print(sortsell) # 내림차순

    #print(sortsell[0])
    for i in range(sell_len):

        if sell[i] == sortsell[0]:
            print(i)
            #print(max_v)

    """
    max 값 전까지 카운트 하고 맥스값에 팔아
    그 이후 다시 맥스값전까지 사고 맥스값에 팔아

    """

