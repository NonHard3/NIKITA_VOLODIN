def get_access_voting(age, is_citizen, is_disqualified):
    if age >= 18 and is_citizen and not is_disqualified:
        print("Вы допущены к голосованию\n")
    else:
        print("В доступе к голосованию отказано! Так как:")
        if age < 18 and age >= 0:
            print("- Вы несовершеннолетний")
        else:
            print("- Введен некорректный возраст")
        if not is_citizen:
            print("- У вас нет гражданства")
        if is_disqualified:
            print("- Что-то с вами не так")
        print()

def test_get_access_voting():
    get_access_voting(25, True, False)
    get_access_voting(15, True, False)
    get_access_voting(-15, True, False)
    get_access_voting(18, False, False)
    get_access_voting(25, True, True)
    get_access_voting(15, False, True)

test_get_access_voting()