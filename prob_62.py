
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
    

cube_set = set()

digit_num = 4
num = 10
cube = num ** 3

while len(str(cube)) == digit_num:
    cube_set.add(str(cube))
    num += 1
    cube = num ** 3
    
# for i in cube_set:
#     chk_set = set(''.join(p) for p in itt.permutations(i, digit_num))
#     if len(chk_set & cube_set) == 5:
#         print (chk_set & cube_set)
    
    
cube_set = set()
digit_num += 1



chk_digit = dict()
for i in cube_set:
    chk = chk_num(i)
    if chk in chk_digit:
        chk_digit[chk] += 1
    else:
        chk_digit[chk] = 1
    
for i in chk_digit:
    if chk_digit[i] == 5:
        print(i)
    
