import math
def f11(x):
    return x**5-x**4/61-((26*x**6+31*x**2)**7+math.cos(x))-(math.log(x**6)+63*x**5)/(x**5-x**3)

print(f'{f11(-89):.2e}',f'{f11(-4):.2e}',sep='\n')