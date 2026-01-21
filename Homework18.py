def get_access_voting(age, is_citizen, is_disqualified):
    if age >= 18 and is_citizen and not is_disqualified:
        print("Вы допущены к голосованию\n")
    else:
        print("В доступе к голосованию отказано! Так как:")
        if age < 18:
            print("- Вы несовершеннолетний")
        if not is_citizen:
            print("- У вас нет гражданства")
        if is_disqualified:
            print("- Что-то с вами не так")
        print()


def input_age():
    global age
    try:
        value = int(input("Введите ваш возраст: "))
    except ValueError:
        print("Введено нечисловое значение! Попробуйте ещё раз")
        input_age()
    else:
        age = value


def input_citizen():
    global is_citizen
    answer = input("""У вас есть гражданство?
Введите Да или Нет: """)
    if answer == "Да" or answer == "да":
        is_citizen = True
    elif answer == "Нет" or answer == "нет":
        is_citizen = False
    else:
        print("Неверное значение!")
        input_citizen()


def input_disqualified():
    global is_disqualified
    answer = input("""У вас есть/была судимость?
Введите Да или Нет: """)
    if answer == "Да" or answer == "да":
        is_disqualified = True
    elif answer == "Нет" or answer == "нет":
        is_disqualified = False
    else:
        print("Неверное значение!")
        input_disqualified()


age = 0
is_citizen = None
is_disqualified = None

input_age()
input_citizen()
input_disqualified()

get_access_voting(age, is_citizen, is_disqualified)
