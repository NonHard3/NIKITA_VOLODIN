def book_list_view(dict_library):
    if len(dict_library) > 0:
        print("Список книг: ")
        for key in dict_library:
            print(key)
    else:
        print("Библиотека пуста")


library = {
    'Скотный двор': {'author': '', 'year': '', 'is_availability': ''},
    '1984': {'author': '', 'year': '', 'is_availability': ''},
    'Мартин Иден': {'author': '', 'year': '', 'is_availability': ''},
    'Сталкер. Тени Чернобыля': {'author': '', 'year': '', 'is_availability': ''},
    'Теория игр': {'author': '', 'year': '', 'is_availability': ''},
}
library_1 = {}

book_list_view(library)
print()
book_list_view(library_1)