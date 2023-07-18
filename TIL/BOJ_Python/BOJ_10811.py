n , m = map(int,input().split())
bas = list[i for i in range(1,n+1)]
for k in range(m):
    a , b = map(int,input().split())
    bas[a-1:b] = bas[b:a-1]
for p in range(n):
    print(bas[p], end=" ")      
