def input_number(message):
    while True:
        try:
            user_number = int(input(message))
        except ValueError:
            print("Введено нечисловое значение! Попробуйте ещё раз")
        else:
            return user_number


def input_grade(message):
    while True:
        user_grade = input_number(message)
        if 0 <= user_grade <= 100:
            return user_grade
        else:
            print("Неверное значение!")


def check_len(function, input_list):
    if len(input_list) > 0:
        function(input_list)
    else:
        print("\nСписок учеников пуст")


def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return 0


def calculate_average_all_students(list_students):
    sum_grades = [calculate_average(student['grades']) for student in list_students]
    print(f"\nОбщий средний балл: {(sum(sum_grades) / len(list_students)):.2f}")


def print_info_about_students(list_students):
    for student in list_students:
        print(
            f"""\nСтудент: {student['name']}
Средний балл: {calculate_average(student['grades']):.2f}
Статус: {"Успешен" if (calculate_average(student['grades'])) >= 75 else "Отстающий"}"""
        )


def add_new_student(list_students):
    dict_student = {'name': input("\nВведите имя нового студента: "), 'grades': []}
    for i in range(input_number("Введите количество оценок: ")):
        dict_student['grades'].append(input_grade("Введите оценку: "))
    list_students.append(dict_student)
    print(
        f"\nДобавлен студент {dict_student.get('name')} со средним баллом {calculate_average(dict_student['grades']):.2f}")
    calculate_average_all_students(list_students)


def remove_worst_student(list_students):
    index_student = 0
    grades_worst = 100
    for student in list_students:
        current_grade = calculate_average(student['grades'])
        if current_grade < grades_worst:
            index_student = list_students.index(student)
            grades_worst = current_grade

    print(
        f"\nСтудент {list_students[index_student].get('name')} со средним баллом {grades_worst:.2f} удален из списка студентов")
    list_students.pop(index_student)
    check_len(calculate_average_all_students, list_students)


def launch_menu(list_students):
    dict_menu = {
        '1': ["Информация об учениках", lambda: check_len(print_info_about_students, list_students)],
        '2': ["Показать средний балл", lambda: check_len(calculate_average_all_students, list_students)],
        '3': ["Добавить нового студента", lambda: add_new_student(list_students)],
        '4': ["Убрать худшего студента", lambda: check_len(remove_worst_student, list_students)],
        '5': ["Завершить работу", ]
    }
    while True:
        print("\nСписок команд: ")
        for key, value in dict_menu.items():
            print(f"{key}.{value[0]}")
        input_user = input("\nВаш выбор: ")
        if input_user in dict_menu and input_user != "5":
            dict_menu[input_user][1]()
        elif input_user == "5":
            break
        else:
            print("\nНеверная команда")


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

launch_menu(students)
