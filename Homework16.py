def get_length_and_type(example):
    try:
        print(f"Тип данных: {type(example)}, длина объекта: {len(example)}\n")
    except TypeError:
        print(f"Для типа данных {type(example)} функция len не работает\n")


int_type = 123
float_type = 123.45
string_type = "987"
list_type = [1, 2, 3, 45]
tuple_type = (1, 2, 3, 12, 435, 2)
dict_type = {"first_name": "Nikita", "last_name": "Volodin", "age": 28}
set_type = {1, 2}

get_length_and_type(int_type)
get_length_and_type(float_type)
get_length_and_type(string_type)
get_length_and_type(list_type)
get_length_and_type(tuple_type)
get_length_and_type(dict_type)
get_length_and_type(set_type)
