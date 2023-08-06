arr = [1,4,5,9,8,7,3,21,6,54]
n = len(arr)


def counting(arr):
    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1

    for l in range(len(count)):
        if (count[l] != 0):
            for j in range(len(count)):
                print(l)
a = counting(arr)


