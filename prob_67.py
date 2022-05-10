
lst = []
f = open("C:/Users/yuhs19/Downloads/p067_triangle.txt", 'r')

for i in f:
    ls = i.split()
    
    lst00 = []
    for j in ls:
        lst00.append(int(j))
        
    lst.append(lst00)
f.close()
        

def rtn_path(i, j):
    #i = 98
    #j = 1
    if i < 99:
        forw = rtn_path(i+1, j)
        back = rtn_path(i+1, j+1)
        if forw > back:
            return lst[i][j] + forw
        else:
            return lst[i][j] + back
    else:
        return lst[i][j]
    
    
rtn_path(1, 1)
