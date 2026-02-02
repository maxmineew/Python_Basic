guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == 'пришёл':
        if len(guests) < 6:
            name = input("Имя гостя: ")
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print("Прости, но мест нет.")
    elif action == 'ушёл':
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Такого гостя нет на вечеринке.")
    elif action == 'пора спать':
        print("Вечеринка закончилась, все легли спать.")
        break
    else:
        print("Некорректное действие. Попробуйте снова.")

