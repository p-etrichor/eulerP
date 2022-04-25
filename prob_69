# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:06:16 2022

@author: yuhs19
"""

def rtn_(a):
    lst = []
    #a = 6
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            lst.append(i)
            lst.append(a // i)
    
    last_lst = []
    for i in range(1, a+1):
        chk = 0
        for j in lst:
            if chk == 0 and i >= j and i % j == 0:
                chk = 1
        
        if chk == 0:
            last_lst.append(i)

    return len(last_lst)


num = 1
ans = 1
for i in range(990000, 1000001):
    rtn = rtn_(i)
    if i / rtn > ans / num:
        ans = i
        num = rtn
