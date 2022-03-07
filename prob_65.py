

from fractions import Fraction as frac

def make_chain(num, num_max):
    if num == num_max:
        if num % 3 == 0:
            return (num // 3 * 2)
        else:
            return 1
    else:
        if num % 3 == 0:
            return (num // 3 * 2) + frac(1, make_chain(num + 1, num_max))
        else:
            return 1 + frac(1, make_chain(num + 1, num_max))






ans = make_chain(1,100) + 1

sum = 0
for i in str(ans.numerator):
    sum += int(i)
    
print(sum)

