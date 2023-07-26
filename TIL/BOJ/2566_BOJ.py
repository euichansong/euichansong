nlist = []
maxlist = []

for i in range(9):
    num =list(map(int,input().split()))
    nlist.append(num)
    
for i in nlist:
    i = max(i)
    maxlist.append(i)
maxnum = max(maxlist)
   
print(maxnum)

for i in nlist:
    if maxnum in i:
        iindex = nlist.index(i) + 1
        maxindex = i.index(maxnum) + 1
        print(iindex,maxindex)

