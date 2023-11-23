###第一题
def solution(number):
    if number < 0 :
        return 0
    cnt=0
    for ch in range(1,number) :
        if ch%3==0 or ch%5==0 :
            cnt+=ch
    return cnt
###第二题
def duplicate_encode(word):
    s=""
    for ch in word.lower() :
        if word.lower().count(ch)==1 :
            s+='('
        else :
            s+=')'
    return s
###第三题
def valid_braces(string):
    s =[]
    mp ={'}':'{',')':'(',']':'['}
    for ch in string :
        if ch=='[' or ch=='(' or ch=='{' :
            s.append(ch)
        else :
            if(s==[] or mp[ch]!=s[-1]) :
                    return False
            else :
                    s.pop()
    if s==[] :
        return True
    else :
        return False
###第五题
def disemvowel(string_):
    s =['a','e','i','o','u','A','E','I','O','U']
    ss=""
    for ch in string_ :
        f=0
        for ch1 in s :
            if ch==ch1 :
                f=1
        if f==0 :
            ss+=ch
    return ss