blood_types = ['A', 'B', 'O', 'AB', 'O', 'B', 'AB', 'B', 'A', 'O', 'A', 'AB']


dic = {}
for i in blood_types:
    dic.setdefault(i,0)
    dic[i] += 1
    
    

print(dic)

# 결과값 : {’A’ : 3, ‘B’ : 3, ‘O’ : 3, ‘AB’ : 3} 으로 나와야 함

# 1. ’[]‘대괄호로 발류 접근해 풀기
# 2. .get() 이용해 풀기
# 3. .setdefault() 이용해 풀기
