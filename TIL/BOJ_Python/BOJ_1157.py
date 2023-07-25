from collections import Counter
a = input()
lowa = a.lower()
cou = dict(Counter(lowa))

res = [] # 최대값 가지는 소문자 알파벳
for key, value in cou.items():
    if max(cou.values()) == value:
        res.append(key)

if len(res) >= 2:
    print('?')
else:
    print(res[0].upper())























# # 내가 풀던 방식
# a = input()
# lowa = a.lower() # 소문자로 바꾼 단어
# alist = [] # 중복된 알파벳 
# coulist = [] # 카운트된 횟수
# uplist = [] #중복된 알파벳 대문자로 변경
# for i in lowa :
#     if i not in alist:
        
#         alist.append(i)

# for k in alist:
#     cou = lowa.count(k)
#     coulist.append(cou)

# for j in alist:
#     j = j.upper()
#     uplist.append(j)
# ziplist =list(zip(uplist, coulist))
# print(max(ziplist))