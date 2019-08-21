import math
g=int(input())
a=[]
b=[]
for x in range(0,g):
    b.append(1)
for x in range(0,g):
    a.append("")
for x in range(0,g):
    a[x]=[int(i) for i in input().split()]
for x in range(1,g):
    for y in range(x-1,-1,-1):
        if b[y]!=0:
            if abs(a[y][0]-a[x][0])<300:
                if 5>math.sqrt(math.pow((a[x][1]-a[y][1]),2)+math.pow((a[x][2]-a[y][2]),2)):
                    b[x]=0
            else:
                break
for x in range(0,len(b)):
    if b[x]==0:
        print("E_FAILED")
    else:
        print("S_OK")
