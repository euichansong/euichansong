import sys
a , b = map(int,sys.stdin.readline().split())
aa = list(map(int,sys.stdin.readline().split()))
bb = list(map(int,sys.stdin.readline().split()))

amb = list(set(aa) - set(bb))

bma = list(set(bb) - set(aa))

apb = list(set(amb) | set(bma))

print(len(apb))

