a=input().split()
hp=int(a[0])
turn=int(a[1])
for x in range(0,turn):
    a=input().split()
    i=int(a[0])
    h=int(a[1])
    if i == 1:
        hp=hp-h
    elif i==2:
        hp=hp+h
    else:
        hp=hp+h
        maxhp=hp
        break;
print(maxhp)
