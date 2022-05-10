

def get_little_div(a):
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return i
    return 1


def get_divs(a):
    #a = 17
    lst = []
    chk = 0
    while chk == 0:
        rtn = get_little_div(a)
        if rtn == 1:
            chk = 1
            lst.append(a)
        else:
            a = a // rtn
            lst.append(rtn)
    
    return set(lst)

def find_totient(a):
    #a = 6
    lst = [i for i in range(1, a)]
    lst_divs = get_divs(a)
    for i in range(0, len(lst)):
        for j in lst_divs:
            if lst[i] % j == 0:
                lst[i] = 0
    
    settt = set(lst)
    if 0 in settt:
        return len(settt) - 1
    else:
        return len(settt)
                
    
    
#find_totient(999999)


#get_divs(987654321)


num = 1
ans = 1
for i in range(899999, 999999):
    rtn = find_totient(i)
    if i / rtn > ans / num:
        ans = i
        num = rtn
