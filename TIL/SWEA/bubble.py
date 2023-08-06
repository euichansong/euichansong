arr = [1,4,5,9,8,7,3,21,6,54]
n = len(arr)

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j+1], arr[j]



