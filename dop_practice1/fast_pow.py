def fast_pow(x, y):
    a = 1
    while y > 0:
        if y == 1:
            return a * x
        if y % 2 != 0:
            a *= x
        x *= x
        y //= 2
    return a

def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert x ** y == fast_pow(x, y)
    print("fast_pow: Тесты пройдены успешно")

test_fast_pow()