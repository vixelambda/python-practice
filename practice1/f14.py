import math
def f14(n):
    if n==0:
        return 2
    else:
        return math.cos(f14(n-1))+math.sin(f14(n-1))