t = int(input())

for i in range(t):
    b = input()
    if len(b) == 1:
        print(b[0]*2)
    else:
        print(b[0]+b[-1])