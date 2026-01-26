def book_list_view(dict_library):
    if not dict_library:
        print("Библиотека пуста")
        return
    else:
        print("Список книг: ")
        for key in dict_library:
            print(key)


library = {
    'Скотный двор': {'author': 'Джордж Оруэлл', 'year': 2001, 'is_availability': False},
    '1984': {'author': 'Джордж Оруэлл', 'year': 1995, 'is_availability': True},
    'Мартин Иден': {'author': 'Джек Лондон', 'year': 2010, 'is_availability': True},
    '451 градус по Фаренгейту': {'author': 'Рэй Брэдбери', 'year': 2005, 'is_availability': True},
    'Оно': {'author': 'Стивен Кинг', 'year': 1990, 'is_availability': False},
}
library_1 = {}

book_list_view(library)
print()
book_list_view(library_1)