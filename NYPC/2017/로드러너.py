c=int(input())
b=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
tmp=list(a)
tmp2=list(b)
arr=[]
a.sort()
d=0
count=0
for x in range(0,len(tmp)):
    for y in range(0,len(a)):
        if a[x]==tmp[y]:
            d=tmp2[tmp.index(tmp[y])]
            b[x]=d
for x in range(len(b)-1,0,-1):
    if b[x]<=x-1:
        count=-1
        break;
    for y in range(x-1,-1,-1):
        if b[x]<=b[y]:
            while b[x]<=b[y]:
                b[y]=b[y]-1
                count=count+1
print(count)
