t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    #print(arr)
    max_v = 0

    res = []
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                count += 1
        res.append(count)
    for k in res:
        if max_v < k:
            max_v = k
    print(f'#{tc} {max_v}')