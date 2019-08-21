#으어어어
a=input().split()
N=int(a[0])
M=int(a[1])
winrate=[0 for x in range(N)]
loserate=[0 for x in range(N)]
group={}
count=0
for x in range(M):
    a=input().split()
    winrate[int(a[0])-1]=winrate[int(a[0])-1]+1
    loserate[int(a[1])-1]=loserate[int(a[1])-1]+1
    for x in range(count):
        if group[x].count(a[0])>0:
            group1=x
            break;
