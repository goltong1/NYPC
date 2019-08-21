i=input().split()
a=int(i[0])
b=int(i[1])
cnt=0
for x in range(a,b+1):
    for y in range(1,x):
        if y*y>x:
            break;
        if x%y==0:
            cnt=cnt+1
            if y*y<x:
                cnt=cnt+1
print(cnt)
