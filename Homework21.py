password = "password123"

while True:
    input_password = input("Введите ваш пароль: ")
    if password == input_password:
        print("Вы вошли в систему. Добро пожаловать!")
        break
    else:
        print("Неправильный пароль. Попробуйте ещё раз")