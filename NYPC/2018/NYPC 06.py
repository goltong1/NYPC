arr=input().split()
a=1
b=0
logic=1
n=int(arr[0])
m=int(arr[1])
while True:
    if (n==1 and m==0)or(n==1 and m==1):
        logic=0
        break;
    if n<=0 or m<=0:
        logic=1
        break;
    if n>m:
        n=n-m
    else:
        m=m-n


if logic==0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
