# a = int(input())
# count = 0
# for i in range(a):
#     text = list(str(input())) # ['h', 'a', 'p', 'p', 'y']
    
    
#     while True :
#         poplist = []
#         for i in range(len(text)):
#             adpop = text.pop(0)
#             poplist.append(adpop)
#             if adpop in poplist:
#                 poplist.clear()
#                 break
#             else:
#                 count += 1
# print(count)

"""
    각 앞의 문자열이 다르면 카운트 같으면 카운트 안함

    문자열을 리스트로 만들어서 pop [i] in 반환값 에 있으면 카운트 안함
    while 리스트 비어있으면 종료 카운트 1
    만약 반환값에 있으면 카운트 안함
    반환값 리스트는 다 종료되면 클리어로 지운다

    
"""

a = int(input())
count = a
for i in range(a):
    text = list(str(input()))  # ['h', 'a', 'p', 'p', 'y']

    poplist = []
    for i in range(len(text)-1):
        if len(text) == 1:
            continue
        # print(text)
        adpop = text.pop(0)
        poplist.append(adpop)
        print(poplist)

        print(text)
        if poplist in text:
            poplist.clear()
            count -= 1

        # print(text)
        # print(adpop)
print(count)