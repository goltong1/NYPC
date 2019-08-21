"""
odd=0
odd_n=0
arr=[]
def checking():
    cnt=0
    for y in arr:
        cnt=cnt+y/2
    cnt=pac(int(cnt))
    for x in arr:
        cnt=cnt/(pac(int(x/2)))
    print(int(cnt))
def pac(n):
    r=1
    for x in range(n):
        r=r*(x+1)
    return r


for x in list(set(tmp)):
    arr.append(tmp.count(x))
    if tmp.count(x)%2!=0:
        odd=odd+1
        odd_n=tmp.count(x)
if odd==0 or odd==1:
    if odd_n>0:
        arr[arr.index(odd_n)]=arr[arr.index(odd_n)]-1
    checking()

else:
    print(0)
"""
string=input()
cnt=0
length=0
if len(string)%2==0:
    center=int(len(string)/2)
else:
    center=int(len(string)/2)+1
length=int(len(string)/2)
for x in range(len(string)):
    tmp=string[x:]+string[:x]
    if tmp[:length]==(tmp[center:])[::-1]:
        cnt=cnt+1
print(cnt)
