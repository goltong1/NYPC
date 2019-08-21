from itertools import combinations
st=int(input())
c=int(input())
arr=[]
for x in range(0,c):
    arr.append(input().split())
arr2=[]
for y in range(0,len(arr)):
    arr[y]=[int(x) for x in arr[y]]
for x in range(0,len(arr)):
    cnt=arr[x][0]
    for y in range(0,len(arr)):
        if arr[y][0]==cnt:
            if arr[x][1]>arr[y][1]:
                tmp=arr[x]
            else:
                tmp=arr[y]
    arr2.append(tmp)
arr3=[]
arr4=[]
for x in range(1,len(arr2)+1):
    tmp=(list(combinations(arr2,x)))
    for y in tmp:
        arr3.append(y)
for x in range(0,len(arr3)):
    cnt=0
    for y in range(0,len(arr3[x])):
        cnt=cnt+arr3[x][y][0]
    if cnt<=st:
        arr4.append(arr3[x])
best=0
bests=[]
for x in range(0,len(arr4)):
    cnt=0
    for y in range(0,len(arr4[x])):
        cnt=cnt+arr4[x][y][1]
    if best<=cnt:
        best=cnt
        bestindex=x
print(best)
print(len(arr4[bestindex]))
for y in range(0,len(arr4[bestindex])):
            bests.append(arr.index(arr4[bestindex][y])+1)
for x in bests:
    print(x,end=' ')
