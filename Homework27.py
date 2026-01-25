my_list = []

print("Для добавления в список вводите любые значения или Stop/Стоп, чтобы остановить ввод")
while True:
    value = input("Введите значение: ")
    if value.lower() == "stop" or value.lower() == "стоп":
        break
    else:
        my_list.append(value)

print(len(set(my_list)))
