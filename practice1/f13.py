import math
def f13(n,m):
    sum1=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            sum1+=33*j+57*j**5+20
    sum2=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            sum2+=i**5+math.exp(j)
    return sum1/31+sum2