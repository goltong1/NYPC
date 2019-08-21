def change_d(d,t):
    for x in range(t):
        d=d+1
        if d>3:
            d=0
    return d
def move(x,y,d):
    if d==0:
        x=x+1
    elif d==1:
        y=y-1
    elif d==2:
        x=x-1
    else:
        y=y+1
    return(x,y)
a=input.split()
N=int(a[0])
M=int(a[1])
T=int(a[2])
x=int(a[3])
y=int(a[4])
arr=[]
answer=[]
for x in range(N):
    a=input().split()
    a=list(map(int,arr))
    arr.append(a)
    answer.append(0)
for x in arr:
    for y in arr[x]:
        arr[x][y]=change_d(arr[x][y],T)
while True:
    i
