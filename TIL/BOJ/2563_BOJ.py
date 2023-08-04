n = int(input())
arr = []
count = 0
for p in range(100):
    row = []
    for o in range(100):
        row.append(0)
    arr.append(row)

for q in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if arr[i][j] == 0:
                arr[i][j] += 1
            else:
                arr[i][j] = 1
            if arr[i][j] == 1:
                count += 1

print(count)


