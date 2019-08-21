#졸려
a=input().split()
N=int(a[0])
m=int(a[1])
first=int(a[2])
status=[0 for x in range(N)]
def umbrella_is_there(n):
    if status[n]!=0:
        return True
    else:
        return False
count=0
haveU=False
now_P=first
for x in range(m):
    a=input().split()
    n=int(a[0])
    needs=int(a[1])
    if needs==0:
        if haveU==True:
            status[now_P-1]=status[now_P-1]+1
            haveU=False
    else:
        if haveU==False:
            if umbrella_is_there(now_P-1)==False:
                count=count+1
            else:
                status[now_P-1]=status[now_P-1]-1
            haveU=True

    now_P=n-1
print(count)
