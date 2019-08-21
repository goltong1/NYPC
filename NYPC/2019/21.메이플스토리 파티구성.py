a=input().split()
N=int(a[0])
Q=int(a[1])
arr_string=input().split()
for x in range(Q):
    arr=input().split()
    arr=list(map(int,arr))
    tmp=set(arr_string[arr[0]-1:arr[1]])
    tmp2=set(arr_string[arr[2]-1:arr[3]])
    if tmp==tmp2:
        print('YES')
    else:
        print('NO')
