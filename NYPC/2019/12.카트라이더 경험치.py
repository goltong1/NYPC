from itertools import permutations
from copy import deepcopy 
a=int(input())
arr=[]
for x in range(a):
    s=input().split()
    arr.append(list(map(int,s)))
tmp=[]
tmp=permutations([x for x in range(len(arr))])
best=0
tmp2=[]
for y in range(len(tmp)):
    cnt=0
    tmp2=deepcopy(arr)
    for x in tmp[y]:
        cnt=sum(tmp2[x])+cnt
        for z in range(len(tmp2)):
            tmp2[z][x]=0
    if cnt>=best:
        best=cnt
print(best)
