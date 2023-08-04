n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(n):
        # print(arr[i][j])
        # print(arr[j][i])
        if arr[i][j] == arr[j][i]:
            res = 1
        else:
            res = 2
            break
if res == 1:
    print("YES")
elif res == 2:
    print("NO")