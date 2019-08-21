from itertools import combinations
a=input().split()
N=int(a[0])
K=int(a[1])
C=int(a[2])
items=[]
for x in range(K):
    for y in range(K):
        items.append([x,y])
colors=combinations(items,N)
"""
for item in colors:
    cnt=0
    per=combinations(item,2)
    for y in per:
        if (((y[0][0]-y[1][0])**2+(y[0][1]-y[1][1])**2)**0.5)<C:
            break;
        cnt=cnt+1
    if cnt==N:
        final=item
        break;
for x in final:
    print(str(x[0])+" "+str(x[1]))
"""
"""
a=input().split()
N=int(a[0])
K=int(a[1])
C=int(a[2])
colors=[]
for x in range(K):
    for y in range(K):
        colors.append([x,y])
"""
