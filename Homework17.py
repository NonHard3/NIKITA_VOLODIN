def max_number(a, b):
    return (a + b + abs(a - b)) / 2


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def test_max_number():
    assert max_number(1, 2) == 2, "Ошибка: максимальное число из (1, 2) является 2"
    assert max_number(6, 3) == 6, "Ошибка: максимальное число из (6, 3) является 6"
    assert max_number(6, 6) == 6, "Ошибка: максимальное число из (6, 6) является 6"
    print("Тесты пройдены")


for x in even_numbers(11):
    print(x)

test_max_number()
