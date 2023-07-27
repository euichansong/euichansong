# t = int(input())
# relist = []
# for i in range(t):
#     r, s = input().split()
    
#     for k in range(int(r)):
#         a= s[k]*int(r)
#         relist.append(a)
        
# print(relist)
"""
2
3 ABC
5 /HTP
"""

# t = int(input())

# for i in range(t):
#     r, s = input().split()
    
#     for k in range(int(r)):
#         print(s[k]*int(r), end='')
#     print()

# t = int(input())

# for i in range(t):
#     r, s = input().split()
#     r = int(r)
#     text = ''
#     for k in range(r):
#         text += r * s
#     print(text)

# t = int(input())

# for i in range(t):
#     r, s = input().split()
#     if i == t:
#         for k in range(int(r)):
#             print(s[k]*int(r), end='')
#     print()

t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    # for k in range(r):
    z=len(s)
    for j in range(z):
        print(s[j]*r, end='')
    print()