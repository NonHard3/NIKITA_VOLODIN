def input_number():
    try:
        number = int(input("Введите число для обратного отсчета: "))
    except ValueError:
        print("Введено нечисловое значение! Попробуйте ещё раз")
        input_number()
    else:
        start_countdown(number)


def start_countdown(number):
    while number >= 0:
        print(number)
        number -= 1


input_number()
