t= int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    count = 0
    for i in range(1 << len(arr)):
        subsetlist = []
        sum1 = 0
        for j in range(len(arr)):
            if i & (1 << j):
                subsetlist.append(arr[j])
                sum1 += arr[j]
        if sum1  == 0:
            count += 1
    print(subsetlist, sum1)

    print(f'#{tc} {count}')
