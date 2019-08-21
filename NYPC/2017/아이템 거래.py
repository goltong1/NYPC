i=[]
g=[]
t=[]
p=int(input())
for x in range(0,p):
    tmp=list(input())[1:]
    i.append(tmp)
cnt=int(input())
for x in range(0,cnt):
    tmp=list(input())
    g.append(tmp)
for x in range(0,cnt):
    if g[x][0]=="B":
        t.append([g[x][2],g[x][3]])
    elif g[x][0]=="M":

    elif g[x][0]=="E":

    else:
        t.remove(t[g[x][1]])
for x in range(0,p):
    print(str(i[x])[1:len(str(i[x]))-2])
