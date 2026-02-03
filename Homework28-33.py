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


library = {
    'Скотный двор': {'author': 'Джордж Оруэлл', 'year': 2001, 'is_availability': False},
    '1984': {'author': 'Джордж Оруэлл', 'year': 1995, 'is_availability': True},
    'Мартин Иден': {'author': 'Джек Лондон', 'year': 2010, 'is_availability': True},
    '451 градус по Фаренгейту': {'author': 'Рэй Брэдбери', 'year': 2005, 'is_availability': True},
    'Оно': {'author': 'Стивен Кинг', 'year': 1990, 'is_availability': False},
}

book_list_view(library)

issue_book(library, '1984')
issue_book(library, 'Скотный двор')
issue_book(library, 'Скотный')

return_book(library, 'Оно')
return_book(library, 'Мартин Иден')
return_book(library, 'Мартин')
