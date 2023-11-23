###第一题
import math
def nearest_sq(n):
    x=int(math.sqrt(n))
    if x**2==n:
        return n
    else :
        if n-x**2<(x+1)**2-n :
            return x**2
        else :
            return (x+1)**2


###第二题
def bouncing_ball(h, bounce, window):
    cnt=1
    if h<=0 or bounce<=0 or bounce>=1 or window >= h :
        return -1
    else :
        while True :
            h=h*bounce
            if h<=window :
                break
            else :
                cnt+=2
        return cnt
    
###第三题
def get_count(sentence):
    cnt=0
    for ch in sentence:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
            cnt=cnt+1
    return cnt
###第四题
def even_or_odd(number):
    if number%2==0 :
        return 'Even'
    else :
        return 'Odd'

