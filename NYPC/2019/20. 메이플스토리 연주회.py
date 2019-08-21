from itertools import combinations
N=int(input())
arr=[]
for x in range(N):
    s=input()
    arr.append(s)
P=list(input())
All=P
cnt=0
for x in range(len(arr)):
    strings=combinations(arr,x)
    for y in strings:
        
print(cnt%1A000000007)
