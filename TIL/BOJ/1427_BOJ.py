a = input()
alist = []
for i in a:
    alist.append(i)

b = list(reversed(sorted(alist)))
c = ''.join(b)
print(c)