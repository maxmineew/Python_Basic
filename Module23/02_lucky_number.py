import random


def main():
    total = 0

    try:
        while total < 777:
            try:
                number = int(input("Введите число: "))
            except ValueError:
                print("Ошибка! Введите целое число.")
                continue

            # Проверка на вероятность 1/13 для вызова исключения
            if random.randint(1, 13) == 13:
                raise Exception("Случайное исключение!")

            # Запись в файл
            with open('out_file.txt', 'a', encoding='utf-8') as file:
                file.write(f"{number}\n")

            total += number

        print("Вы успешно выполнили условие для выхода из порочного цикла!")

    except Exception:
        print("Вас постигла неудача!")


if __name__ == "__main__":
    main()