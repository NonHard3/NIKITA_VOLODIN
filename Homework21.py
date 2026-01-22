password = "password123"

while True:
    print("Введите ваш пароль: ", end="")
    input_password = input()
    if password == input_password:
        print("Вы вошли в систему. Добро пожаловать!")
        break
    else:
        print("Неправильный пароль. Попробуйте ещё раз")