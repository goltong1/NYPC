import re
wu=input()
def judge(m):
    if str(m)=='None':
        print("No")
    else:
        print("Yes")
p = re.compile("^([a-zA-Z0-9.-])+@([a-zA-Z0-9.-])+$")
for x in range(0,int(wu)):
    nya=input()
    m = p.match(nya)
    judge(m)
