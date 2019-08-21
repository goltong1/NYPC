def f(sen,a,b):
    x=len(sen)
    for i in range(1,(x//2)+1):
        if x%i==0:
            s=sen[0:i]
            count=int(x/i)
            if count<a:
                return 3
            elif count>b:
                return 1
    return 2
g=input().split()
for x in range(0,len(g)):
    g[x]=int(g[x])
s=input()

print(f(s,g[1],g[2]))
