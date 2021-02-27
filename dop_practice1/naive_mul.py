def naive_mul(x, y):
    a = 0
    for i in range(0, y):
        a += x
    return a

def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert x * y == naive_mul(x, y)
    print("naive_mul: Тесты пройдены успешно")

test_naive_mul()