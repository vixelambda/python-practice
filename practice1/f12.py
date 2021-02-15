def f12(x):
    if x<71:
        return 33*x+57*x**5+20
    elif 71<=x<148:
        return 11*x**4+41*x**6+24
    else:
        return x**3/53-73*x**7

print(f'{f12(93):.2e}',f'{f12(213):.2e}',sep='\n')