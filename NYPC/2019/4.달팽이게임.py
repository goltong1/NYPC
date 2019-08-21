a=input().split()
rin=int(a[0])
count=0
saber=int(a[1])
direction_x=True
direction_y=True
X=1
Y=1
def move_x(x):
    if direction_x:
        x=x+1
    else:
        x=x-1
    return x
def move_y(y):
    if direction_y:
        y=y+1
    else:
        y=y-1
    return y
move=True
Max_x=rin
Min_x=1
Max_y=rin
Min_y=2
while True:
    if count==saber-1:
        break;
    if move:
        X=move_x(X)
    else:
        Y=move_y(Y)
    if move and X>=Max_x and direction_x:
        move=False
        direction_x=False
        Max_x=Max_x-1
    elif move and X<=Min_x and not direction_x:
        move=False
        direction_x=True
        Min_x=Min_x+1
    elif not move and Y>=Max_y and direction_y:
        move=True
        direction_y=False
        Max_y=Max_y-1
    elif not move and Y<=Min_y and not direction_y:
        move=True
        direction_y=True
        Min_y=Min_y+1
    count=count+1
print(X,Y)
