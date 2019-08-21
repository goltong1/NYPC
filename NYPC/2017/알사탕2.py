a=int(input())
b=[]
c=[]
cnt=0
for x in range(0,a):
    b.append([])
for x in range(0,a):
    b[x].append(int(input()))
    b[x].append(list(input()))
    b[x].append(list(input()))
for x in range(0,len(b)):
    tmp=b[x][2]
    cnt=0
    for y in range(0,len(b[x][2])):
        if b[x][2][y]==b[x][1][0]:
            cnt=cnt+1
            old=b[x][1]
            b[x][1].remove(b[x][1][0])
        elif b[x][2][y]==b[x][1][len(b[x][1])-1]:
            cnt=cnt+1
            old=b[x][1]
            b[x][1].remove(b[x][1][len(b[x][1])-1])
        else:
            b[x][1]=old
            if b[x][2][y]==b[x][1][len(b[x][1])-1]:
                cnt=cnt+1
                b[x][1].remove(b[x][1][len(b[x][1])-1])
            elif b[x][2][y]==b[x][1][0]:
                cnt=cnt+1
                b[x][1].remove(b[x][1][0])
            else:
                break;
    if cnt==len(b[x][2]):
        c.append(1)
    else:
        c.append(0)
for x in range(0,len(c)):
    print(c[x])
