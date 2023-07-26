alpha = 'abcdefghijklmnopqrstuvwxyz'
alphalist = list(str(alpha))
text = input()

for i in alphalist:
    a = text.find(i)
    print(a, end=' ')