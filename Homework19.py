def convert_number_to_text(number):
    if 0 < number <= 5:
        text = ""
        if number == 1:
            text = "One"
        if number == 2:
            text = "Two"
        if number == 3:
            text = "Three"
        if number == 4:
            text = "Four"
        if number == 5:
            text = "Five"
        print("Соответствующее слово: " + text)
    else:
        print("Число вне диапазона! Попробуйте ещё раз")
        input_number()


def input_number():
    try:
        convert_number_to_text(int(input("Введите число от 1 до 5: ")))
    except ValueError:
        print("Введено нечисловое значение! Попробуйте ещё раз")
        input_number()


input_number()
