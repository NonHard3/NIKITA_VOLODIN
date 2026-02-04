def input_year(message):
    while True:
        try:
            user_number = int(input(message))
        except ValueError:
            print("Введено нечисловое значение! Попробуйте ещё раз")
        else:
            if 1900 <= user_number <= 2026:
                return user_number
            else:
                print("Введен некорректный год издания! Попробуйте ещё раз")


def input_agreement(message):
    list_agreement = ["да", "yes", "lf", "нуы"]
    list_refusal = ["нет", "no", "ytn", "тщ"]
    while True:
        user_agreement = input(message)
        if user_agreement.lower() in list_agreement:
            return True
        elif user_agreement.lower() in list_refusal:
            return False
        else:
            print("Некорректный ответ")


def book_list_view(dict_library):
    if not dict_library:
        print("\nБиблиотека пуста")
        return
    else:
        print("\nСписок книг: ")
        for key in dict_library:
            print(key)


def add_book(dict_library, title, author, year):
    if title not in dict_library:
        dict_library[title] = dict(author=author, year=year, is_availability=None)
        print(f"\nКнига '{title}' добавлена в библиотеку")
    else:
        print("\nДанная книга уже есть в библиотеке")
        agreement = input_agreement("Обновить информацию о книге? (Да/Нет): ")
        if agreement:
            dict_library[title]['author'] = author
            dict_library[title]['year'] = year
            print("Информация обновлена")
        else:
            return


def remove_book(dict_library, title):
    if title in dict_library:
        del dict_library[title]
        print(f"\nКнига '{title}' удалена из библиотеки")
    else:
        print(f"\nКнига '{title}' не найдена в библиотеке")


def issue_book(dict_library, title):
    if title not in dict_library:
        print(f"\nОшибка. Такой книги нет в библиотеке")
    elif not dict_library[title]['is_availability']:
        print(f"\nОшибка. Книга '{title}' уже выдана")
    else:
        dict_library[title]['is_availability'] = False
        print(f"\nКнига '{title}' выдана читателю")


def return_book(dict_library, title):
    if title not in dict_library:
        print(f"\nОшибка. Такой книги нет в библиотеке")
    elif dict_library[title]['is_availability']:
        print(f"\nОшибка. Книга '{title}' уже в библиотеке")
    else:
        dict_library[title]['is_availability'] = True
        print(f"\nКнига '{title}' возвращена в библиотеку")


def find_book(dict_library, title):
    if title not in dict_library:
        print(f"\nОшибка. Такой книги нет в библиотеке")
        return
    else:
        print(
            f"""\nНазвание книги: {title}
Автор: {dict_library[title]['author']}
Год издания: {dict_library[title]['year']}"""
        )
    if dict_library[title]['is_availability'] is None:
        print("Книга в библиотеке, но ее статус не определен")
    elif not dict_library[title]['is_availability']:
        print("Наличие: Книга выдана")
    else:
        print("Наличие: Книга доступна")


def user_menu(dict_library):
    dict_menu = {
        '1': ("Отобразить список книг", lambda: book_list_view(dict_library)),
        '2': ("Получить информацию о книге", lambda: find_book(dict_library, input("\nВведите название книги: "))),
        '3': ("Добавить/Обновить книгу",
              lambda: add_book(dict_library, input("\nВведите название книги: "), input("Введите автора: "),
                               input_year("Введите год издания: "))),
        '4': ("Удалить книгу", lambda: remove_book(dict_library, input("\nВведите название книги: "))),
        '5': ("Выдать книгу", lambda: issue_book(dict_library, input("\nВведите название книги: "))),
        '6': ("Вернуть книгу", lambda: return_book(dict_library, input("\nВведите название книги: "))),
        '7': ("Завершить работу", lambda: None)
    }
    while True:
        print("\nСписок команд: ")
        for key, value in dict_menu.items():
            print(f"{key}.{value[0]}")
        input_user = input("\nВаш выбор: ")
        if input_user in dict_menu and input_user != "7":
             dict_menu[input_user][1]()
        elif input_user == "7":
            break
        else:
            print("\nНеверная команда")


library = {
    'Скотный двор': {'author': 'Джордж Оруэлл', 'year': 2001, 'is_availability': False},
    '1984': {'author': 'Джордж Оруэлл', 'year': 1995, 'is_availability': True},
    'Мартин Иден': {'author': 'Джек Лондон', 'year': 2010, 'is_availability': True},
    '451 градус по Фаренгейту': {'author': 'Рэй Брэдбери', 'year': 2005, 'is_availability': True},
    'Оно': {'author': 'Стивен Кинг', 'year': 1990, 'is_availability': False},
}

user_menu(library)