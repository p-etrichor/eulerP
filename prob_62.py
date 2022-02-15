
import itertools as itt


def chk_num(string):
    rtn = ''
    rtn += str(string.count('0'))
    rtn += str(string.count('1'))
    rtn += str(string.count('2'))
    rtn += str(string.count('3'))
    rtn += str(string.count('4'))
    rtn += str(string.count('5'))
    rtn += str(string.count('6'))
    rtn += str(string.count('7'))
    rtn += str(string.count('8'))
    rtn += str(string.count('9'))
    
    return rtn
    
digit_num = 4
num = 10
cube = num ** 3

kkk = 0

while kkk != 1:
    cube_set = set()
    
    while len(str(cube)) == digit_num:
        cube_set.add(str(cube))
        num += 1
        cube = num ** 3
        
    # for i in cube_set:
    #     chk_set = set(''.join(p) for p in itt.permutations(i, digit_num))
    #     if len(chk_set & cube_set) == 5:
    #         print (chk_set & cube_set)
        
        
    
    
    chk_digit = dict()
    for i in cube_set:
        chk = chk_num(i)
        if chk in chk_digit:
            chk_digit[chk].append(i)
        else:
            chk_digit[chk] = list([i])
        
    for i in chk_digit:
        if len(chk_digit[i]) == 5:
            print(chk_digit[i])
            print(min(chk_digit[i]))
            kkk = 1
        
    digit_num += 1
    


