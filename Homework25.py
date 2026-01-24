def input_number(message):
    while True:
        try:
            user_number = int(input(message))
        except ValueError:
            print("Введено нечисловое значение! Попробуйте ещё раз")
        else:
            return user_number


def create_list_numbers(list_type):
    for i in range(len(list_type)):
        number_elements = input_number(f"Введите количество чисел для {i + 1}-ого списка: ")

        for j in range(number_elements):
            list_type[i].append(input_number("Введите число: "))


def sum_list_values(list_type):
    result = []
    for i in range(len(list_type)):
        for j in range(len(list_type[i])):
            try:
                result[j] += list_type[i][j]
            except IndexError:
                result.append(list_type[i][j])

    return result


general_list = [[], []]

create_list_numbers(general_list)
result_list = sum_list_values(general_list)

print(result_list)