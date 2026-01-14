print("Операция сложения")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
except ValueError:
    print("Пользователь ввёл нечисловое значение")
else:
    print(f"Результат сложения: {result}\n")

print("Операция вычитания")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 - num2
except ValueError:
    print("Пользователь ввёл нечисловое значение")
else:
    print(f"Результат вычитания: {result}\n")

print("Операция умножения")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 * num2
except ValueError:
    print("Пользователь ввёл нечисловое значение")
else:
    print(f"Результат умножения: {result}\n")

print("Операция деления")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Пользователь ввёл нечисловое значение")
except ZeroDivisionError:
    print("Делитель не должен быть равным нулю")
else:
    print(f"Результат деления: {result}\n")