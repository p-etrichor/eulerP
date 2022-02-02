
print("what is Github")

def chk_num(x, num):
    k = 1
    chk = 0
    if x == 3:
        while chk < num:
            chk = k*(k+1)/2
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
            chk = k*(3*k-1)/2
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
            chk = k*(5*k-3) / 2
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

for i in range(10):
  print(i)
  
  
  
chk_num(4, 7798)

