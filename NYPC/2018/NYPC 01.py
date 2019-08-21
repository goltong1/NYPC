s=input().split()
t=int(input())
tmp=int(s[0])
tmp2=int(s[1])
g=False
for x in range(0,t//tmp+1):
    for y in range(0,(t-(tmp*x))//tmp2+1):
        hp=x
        if t-tmp*x==y*tmp2:
            mana=y
            g=True
            break;
    if g==True:
        break;
print(hp,mana)
