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


def add_book(title, author, year):
    global library
    if title not in library:
        library[title] = dict(author=author, year=year, is_availability=None)
        print("\nКнига добавлена в библиотеку")
    else:
        print("\nДанная книга уже есть в библиотеке")
        agreement = input_agreement("Обновить информацию о книге? (Да/Нет): ")
        if agreement:
            library[title]['author'] = author
            library[title]['year'] = year
            print("Информация обновлена")
        else:
            return


library = {
    'Скотный двор': {'author': 'Джордж Оруэлл', 'year': 2001, 'is_availability': False},
    '1984': {'author': 'Джордж Оруэлл', 'year': 1995, 'is_availability': True},
    'Мартин Иден': {'author': 'Джек Лондон', 'year': 2010, 'is_availability': True},
    '451 градус по Фаренгейту': {'author': 'Рэй Брэдбери', 'year': 2005, 'is_availability': True},
    'Оно': {'author': 'Стивен Кинг', 'year': 1990, 'is_availability': False},
}
library_1 = {}

book_list_view(library)

add_book("123", "Lincoln", 1955)
add_book("Мартин Иден", "Lincoln", 1955)
add_book(input("\nВведите название книги: "), input("Введите автора: "), input_year("Введите год издания: "))

book_list_view(library)
