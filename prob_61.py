
import itertools as itt

def chk_num(x, num):
    k = 1
    chk = 0
    if x == 3:
        while chk < num:
            chk = k*(k+1)//2
            k += 1
            if chk == num:
                return 3
        return -3
    elif x == 4:
        while chk < num:
            chk = k**2
            k += 1
            if chk == num:
                return 4
        return -4
    elif x == 5:
        while chk < num:
            chk = k*(3*k-1)//2
            k += 1
            if chk == num:
                return 5
        return -5
    elif x == 6:
        while chk < num:
            chk = k*(2*k-1)
            k += 1
            if chk == num:
                return 6
        return -6
    elif x == 7:
        while chk < num:
            chk = k*(5*k-3) // 2
            k += 1
            if chk == num:
                return 7
        return -7
    elif x == 8:
        while chk < num:
            chk = k*(3*k-2)
            k += 1
            if chk == num:
                return 8
        return -8
    else:
        return 0


def chk_true(num):
    lst = []
    for i in range(3, 9):
        if chk_num(i, num) > 0:
            lst.append(i)
    return lst
        
        
#f_lst = [''.join(p) for p in itt.combinations_with_replacement('0123456789', 4)]
t_lst = [''.join(p) for p in itt.product('0123456789', repeat = 2)]

num = 0
hoobo_lst = []


for i in t_lst:
    if int(i) > 9:
        for j in t_lst:
            num = int(i+j)
            if len(chk_true(num)) != 0 and int(j) > 9:
                for k in t_lst:
                    num = int(j+k)
                    if len(chk_true(num)) != 0 and int(k) > 9:
                        # print(num)
                        # num = int(k+i)
                        # if len(chk_true(num)) != 0:
                        #     print(num)
                        #여기가 예제일 때 확인점
                        for l in t_lst:
                            num = int(k+l)
                            if len(chk_true(num)) != 0 and int(l) > 9:
                                for m in t_lst:
                                    num = int(l+m)
                                    if len(chk_true(num)) != 0 and int(m) > 9:
                                        for n in t_lst:
                                            num = int(m+n)
                                            if len(chk_true(num)) != 0 and int(n) > 9:
                                                num = int(n+i)
                                                if len(chk_true(num)) != 0:
                                                    hoobo_lst.append(i+j+k+l+m+n)

real_hoobo = []
for i in hoobo_lst:
    chk_set = set()
    chk_set.update(chk_true(int(i[0:4])))
    chk_set.update(chk_true(int(i[2:6])))
    chk_set.update(chk_true(int(i[4:8])))
    chk_set.update(chk_true(int(i[6:10])))
    chk_set.update(chk_true(int(i[8:12])))
    chk_set.update(chk_true(int(i[10:12] + i[0:2])))
    #print(chk_set)
    
    if len(chk_set) == 6:
        real_hoobo.append(i)
        
        
chk_true(21)
