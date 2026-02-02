def validate_registration_data(line):
    """Валидация строки с данными регистрации."""
    data = line.strip().split()

    # Проверка 1: присутствие всех трех полей
    if len(data) != 3:
        raise IndexError("НЕ присутствуют все три поля")

    name, email, age_str = data

    # Проверка 2: имя содержит только буквы
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")

    # Проверка 3: email содержит @ и точку
    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")

    # Проверка 4: возраст - число от 10 до 99
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")

    if not (10 <= age <= 99):
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")


def process_registrations(input_file, good_file, bad_file):
    """Обработка файла с регистрациями."""
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(good_file, 'w', encoding='utf-8') as good_out, \
            open(bad_file, 'w', encoding='utf-8') as bad_out:

        for line in infile:
            line = line.rstrip('\n')  # Убираем символ новой строки для обработки
            try:
                validate_registration_data(line)
                # Если все проверки пройдены, записываем в good_file
                good_out.write(line + '\n')
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                # Если есть ошибка, записываем в bad_file с указанием ошибки
                bad_out.write(f"{line}\t{str(e)}\n")


# Основная часть программы
if __name__ == "__main__":
    input_filename = "registrations.txt"
    good_filename = "registrations_good.log"
    bad_filename = "registrations_bad.log"

    process_registrations(input_filename, good_filename, bad_filename)

    print(f"Обработка завершена. Проверьте файлы:")
    print(f"- Правильные данные: {good_filename}")
    print(f"- Ошибочные данные: {bad_filename}")


    def create_test_file():
        """Создание тестового файла с различными случаями."""
        test_data = [
            # Правильные данные
            "Василий test@test.ru 27",
            "Геннадий ttdababmt@gmail.com 69",
            "Ольга ysbxur@gmail.com 20",

            # Ошибочные данные
            "Ольга kmrn@gmail.com 123",  # Возраст > 99
            "Чехова kb@gmail.com 142",  # Возраст > 99
            "Степан ky 59",  # Email без @ и точки
            "Иван123 ivan@mail.ru 30",  # Имя содержит цифры
            "Анна annamail.ru 25",  # Email без @
            "Петр petr@mail 35",  # Email без точки
            "Мария maria@gmail.com 5",  # Возраст < 10
            "test@test.ru 30",  # Нет имени
            "Алексей alex@mail.ru",  # Нет возраста
            "Елена elena@gmail.com сто",  # Возраст не число
            "Игорь-Петров igor@gmail.com 40",  # Имя содержит дефис (не только буквы)
            "Анна Мария anna@gmail.com 30",  # Два слова в имени (разделится на 4 части)
        ]

        with open("registrations.txt", "w", encoding="utf-8") as f:
            for line in test_data:
                f.write(line + "\n")

        print("Тестовый файл registrations.txt создан.")

    # Если нужно создать тестовые данные, раскомментируйте следующую строку:
    # create_test_file()