try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Пользователь ввел нечисловое значение")
except ZeroDivisionError:
    print("Делитель не должен быть равным нулю")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена")
