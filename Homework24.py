def swap_first_and_last(list_type):
    list_type[0], list_type[-1] = list_type[-1], list_type[0]
    return list_type


def create_list_str():
    list_str = []

    print("Введите 5 значений:\n")

    for _ in range(5):
        list_str.append(input())

    return list_str


result = swap_first_and_last(create_list_str())

print(result)
