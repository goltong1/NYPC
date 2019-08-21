import re
def ABB(test_keyword) :
    if __name__ == '__main__':
        split_keyword_list = list(test_keyword)
        result = list()
        for keyword in split_keyword_list:
            # 한글 여부 check 후 분리
            if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
                char_code = ord(keyword) - BASE_CODE
                char1 = int(char_code / CHOSUNG)
                char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
                char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
                if char3 == 0: return 1
                else : return 0

d={}
while 1:
    #print(d)
    a=list(input().split(" "))
    if a[0]=="set" :
        d[a[1]]=a[2]
    elif a[0]=="end" : break
    else :
        s=''
        for i in a[1:]:
            #print(i,i[1:-2])
            if i[0]=='{' :
                s+=str(d[i[1:-2]])
                #print(ABB(str(d[i[1:-2]][-1])))
                if ABB(str(d[i[1:-2]][-1])) :
                    if i[-1]=='은' or i[-1]=='는' : s+='는'
                    if i[-1]=='이' or i[-1]=='가' : s+='가'
                    if i[-1]=='을' or i[-1]=='를' : s+='를'
                else :
                    if i[-1]=='은' or i[-1]=='는' : s+='은'
                    if i[-1]=='이' or i[-1]=='가' : s+='이'
                    if i[-1]=='을' or i[-1]=='를' : s+='을'
            else : s+=i
            s+=' '
        print(s[:-1])
