while True:
    # 리스트로 받는다
    a = list(map(int, input()))
    # 0받으면 끝낸다
    if a[0] == 0:
        break
    # a길이//2 범위에서 # 반만 해도 다 구한거다
    for i in range(len(a)//2):
        # 만약 a[i]와 a[-i]가 같지 않으면 palindrome 아니다
        if a[i] != a[-(i+1)]:
            print("no")
            break
    # 만약 a[i]와 a[-i]가 같으면 palindrome
    else:
        print('yes')
