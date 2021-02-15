import math
def f14(n):
    if n==0:
        return 7
    else:
        return 1/18*(f14(n-1))**2-math.sin(f14(n-1))

print(f'{f14(12):.2e}',f'{f14(7):.2e}',sep='\n')