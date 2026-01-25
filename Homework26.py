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


def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_successful_or_not(average_grade):
    result = "Успешен" if average_grade >= 75 else "Отстающий"
    return result


def print_info_about_students(list_students):
    for student in list_students:
        print(f"""Студент: {student['name']}
Средний балл: {calculate_average(student['grades']):.2f}
Статус: {determine_successful_or_not(calculate_average(student['grades']))}\n""")


def calculate_average_all_students(list_students):
    sum_grades = [calculate_average(student['grades']) for student in list_students]
    print(f"Общий средний балл: {(sum(sum_grades) / len(list_students)):.2f}\n")


def add_new_student(list_students):
    dict_student = {'name': input("Введите имя нового студента: "), 'grades': []}
    for i in range(input_number("Введите количество оценок: ")):
        dict_student['grades'].append(input_grade("Введите оценку: "))
    list_students.append(dict_student)
    print(
        f"Добавлен студент {dict_student.get('name')} со средним баллом {calculate_average(dict_student['grades']):.2f}\n")
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
        f"Студент {list_students[index_student].get('name')} со средним баллом {grades_worst:.2f} удален из списка студентов\n")
    list_students.pop(index_student)
    calculate_average_all_students(list_students)


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

print_info_about_students(students)
calculate_average_all_students(students)
add_new_student(students)
remove_worst_student(students)
print_info_about_students(students)
