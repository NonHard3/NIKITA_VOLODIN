def input_number():
    while True:
        try:
            number = int(input("Введите число для обратного отсчета: "))
        except ValueError:
            print("Введено нечисловое значение! Попробуйте ещё раз")
        else:
            break

    return number


def start_countdown(number):
    while number >= 0:
        print(number)
        number -= 1


input_user = input_number()
start_countdown(input_user)
