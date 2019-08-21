eriri=input()
megumi=[]
utaha=input().split()
for x in utaha:
    megumi.append(int(x))
utaha=input().split()
eriri=[]
for y in utaha:
    eriri.append(int(y))
tomoya=-1
for z in range(0,len(eriri)):
    if eriri[z]!=0:
        if tomoya==-1:
            tomoya=megumi[z]/eriri[z]
        if megumi[z]/eriri[z]<=tomoya:
            tomoya=int(megumi[z]/eriri[z])
print(tomoya)
