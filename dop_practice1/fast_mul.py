def fast_mul(x, y):
    if x==0 or y==0:
        return 0
    a = 0
    while y > 0:
        if y % 2 == 1:
            a += x
        x *= 2
        y //= 2
    return a

def test_fast_mul():
    for x in range(101):
        for y in range(101):
            assert x * y == fast_mul(x, y)
    print("fast_mul: Тесты пройдены успешно")

test_fast_mul()