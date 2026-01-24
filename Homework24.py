def swap_first_and_last(list_type):
    first = list_type[0]
    last = list_type[-1]
    list_type[0] = last
    list_type[-1] = first
    return list_type


list_str = []

print("Введите 5 значений:\n")

for _ in range(5):
    list_str.append(input())

swap_first_and_last(list_str)

print(list_str)
