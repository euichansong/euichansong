n , m = map(int,input().split())
bas = [i for i in range(1,n+1)]
for j in range(m):
    a, b = map(int,input().split())
    bas[a-1], bas[b-1] = bas[b-1] , bas[a-1] # 서로 공 위치 교환
for k in bas:
    print(k, end =' ')