n=int(input())
arr=[]
for x in range(0,n):
    arr.append(input().split())
for x in range(0,len(arr)):
    arr[x][0]=int(arr[x][0][0:2])*60+int(arr[x][0][3:])
    arr[x][1]=int(arr[x][1][0:2])*60+int(arr[x][1][3:])

arr2=[]
for x in range(arr[0][0],arr[len(arr)-1][1]+1):
    cnt=0
    for y in range(0,len(arr)):
        if arr[y][0]<=x and arr[y][1]>=x:
            cnt=cnt+1
    arr2.append(cnt)
cnt=0
for x in (arr2.index(max(arr2)),len(arr2)):
    cnt=cnt+1

time=arr2.index(max(arr2))+arr[0][0]
time2=arr2.index(max(arr2))+cnt+arr[0][0]
if (time//60)<10:
    s='0'
else:
    s=''
if -60*(time//60)+(time)<10:
    t='0'
else:
    t=''

print(s+str((time//60))+':'+t+str(-60*(time//60)+(time)),end=' ')
if (time2//60)<10:
    s='0'
else:
    s=''
if -60*(time2//60)+(time2)<10:
    t='0'
else:
    t=''

print(s+str((time2//60))+':'+t+str(-60*(time2//60)+(time2)))
