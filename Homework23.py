sum_number = 0
count_number = 0
user_number = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_number += i

squares = [i ** 2 for i in range(1, 11) if i % 2 != 0]

while True:
    try:
        user_number = int(input("Введите число: "))
    except ValueError:
        print("Введено нечисловое значение! Попробуйте ещё раз")

    if user_number >= 0:
        count_number += 1
    else:
        print("Вы ввели отрицательное число. Цикл завершен\n")
        break

print(f"Сумма четных чисел от 1 до 100: {sum_number}")
print(f"Список квадратов нечетных чисел от 1 до 10: {squares}")
print(f"Количество введенных чисел: {count_number}")
