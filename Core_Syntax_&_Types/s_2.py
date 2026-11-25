# Floor division. Write ceil_div(a, b) that returns the ceiling of a / b for positive integers, using only integer arithmetic (no math, no floats).

def ceil_dev(a,b):
    return (a+b-1)//b

print(ceil_dev(11,3))