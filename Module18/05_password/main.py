def is_strong_password(password):
    if len(password) < 8:
        return False
    if sum(c.isdigit() for c in password) < 3:
        return False
    if not any(c.isupper() for c in password):
        return False
    return True


while True:
    user_password = input("Придумайте пароль: ")

    if is_strong_password(user_password):
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
