from collections import Counter
def change(a,b):
    arr[int(a)-1]=b


def center_check(a,b):
    answer=0
    a=int(a)
    b=int(b)
    count_dic=Counter(arr[a-1:b])
    
    for x in count_dic.keys():
        tmp=count_dic[x]
        if tmp&1:
            answer=x
            break;
        
    return answer
a=input().split()
N=int(a[0])
Q=int(a[1])
arr=input().split()

if N<=100000 or Q<=100000:
    for x in range(Q):
        f=input().split()
        c=f[0]
        a=f[1]
        b=f[2]
        if c=='1':
            change(a,b)
        else:
            print(center_check(a,b))
else:
    print("out!")

