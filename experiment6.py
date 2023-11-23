###第一题:
def count_developers(lst):
    cnt=0
    for i in lst:
        if i['continent']=='Europe' and i['language']=='JavaScript':
            cnt=cnt+1
    return cnt
###第二题：
def zero(fun = None): 
    return fun(0) if fun else 0

def one(fun = None): 
    return fun(1) if fun else 1
        
def two(fun = None): 
    return fun(2) if fun else 2

def three(fun = None): 
    return fun(3) if fun else 3

def four(fun = None): 
    return fun(4) if fun else 4

def five(fun = None): 
    return fun(5) if fun else 5

def six(fun = None): 
    return fun(6) if fun else 6

def seven(fun = None): 
    return fun(7) if fun else 7

def eight(fun = None): 
    return fun(8) if fun else 8

def nine(fun = None): 
    return fun(9) if fun else 9

def plus(y): 
    return lambda x: x+y

def minus(y): 
    return lambda x: x-y

def times(y): 
    return lambda x: x*y

def divided_by(y): 
    return lambda x: x//y
###第三题:
def shorten_number(suffixes, base):
    
    def my_filter(data):
        try:
            number = int(data)
            
        except (TypeError, ValueError):
            return str(data)
        
        else:
            i = 0
            
            while number//base > 0 and i < len(suffixes)-1:
                number //= base
                i += 1
            return str(number) + suffixes[i]     

    return my_filter
###第四题
def find_senior(lst): 
    mage=max(a['age'] for a in lst)
    return [a for a in lst if a['age']==mage]
