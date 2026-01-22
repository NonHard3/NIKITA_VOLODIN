def convert_number_to_text(number):
    if number == 1:
        text = "One"
    elif number == 2:
        text = "Two"
    elif number == 3:
        text = "Three"
    elif number == 4:
        text = "Four"
    elif number == 5:
        text = "Five"
    else:
        print("Число вне диапазона! Попробуйте ещё раз")
        input_number()
        return
    print("Соответствующее слово: " + text)

def input_number():
    try:
        convert_number_to_text(int(input("Введите число от 1 до 5: ")))
    except ValueError:
        print("Введено нечисловое значение! Попробуйте ещё раз")
        input_number()


input_number()
