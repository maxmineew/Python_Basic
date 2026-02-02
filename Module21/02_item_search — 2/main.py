def find_key(data, target_key, max_depth=None, current_depth=0):
    """
    Рекурсивно ищет ключ в словаре с возможным ограничением по глубине.

    Args:
        data (dict): Словарь для поиска
        target_key (str): Искомый ключ
        max_depth (int, optional): Максимальная глубина поиска. None - без ограничений.
        current_depth (int): Текущая глубина рекурсии

    Returns:
        Любой тип: Значение найденного ключа или None
    """
    # Проверяем, не превышена ли максимальная глубина
    if max_depth is not None and current_depth > max_depth:
        return None

    # Если ключ найден на текущем уровне
    if target_key in data:
        return data[target_key]

    # Рекурсивно ищем во вложенных словарях
    for key, value in data.items():
        if isinstance(value, dict):
            result = find_key(value, target_key, max_depth, current_depth + 1)
            if result is not None:
                return result

    return None


def main():
    # Исходный словарь
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    # Ввод искомого ключа
    search_key = input("Введите искомый ключ: ")

    # Запрос о максимальной глубине
    depth_choice = input("Хотите ввести максимальную глубину? Y/N: ").strip().lower()

    max_depth = None
    if depth_choice == 'y':
        try:
            max_depth = int(input("Введите максимальную глубину: "))
        except ValueError:
            print("Ошибка: введите целое число. Установлена максимальная глубина по умолчанию.")
            max_depth = None

    # Поиск ключа
    result = find_key(site, search_key, max_depth)

    # Вывод результата
    print(f"Значение ключа: {result}")


if __name__ == "__main__":
    main()