input_file = open('input5.5.txt','r', encoding='UTF8')
arr=[]
while True:
    c= input_file.readline()
    if not c: break
    arr.append(c)
t=arr[0]
arr=arr[1:]
for x in range(0,len(arr)):
    head=0
    for y in range(0,len(arr[x])):
        if arr[x][y]==' ':
            print(arr[x][head],end='')
            head=y+1
    print(arr[x][head])
