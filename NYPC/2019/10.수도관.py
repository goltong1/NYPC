a=input().split()
n=int(a[0])
e=int(a[1])
cnt=1
x=0
y=0
sticks=[]
for x in range(n):
    a=input().split()
    if (int(a[1])-e)<0:
        Min=0
    else:
        Min=int(a[1])-e
    sticks.append([Min,int(a[1])+e])
checking=False
arr=[]
for x in range(0,len(sticks)):
    if checking:
        arr=[sticks[x-1]]
        checking=False
    for y in arr:
        if y[1]<sticks[x][0]:
            checking=True
            cnt=cnt+1
            break;
        elif y[0]>sticks[x][1]:
            cnt=cnt+1
            checking=True
            break;
    arr.append(sticks[x])
print(cnt)
    
        
