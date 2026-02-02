def flatten(items):
    """Рекурсивно раскладывает вложенные списки в плоский список."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def custom_sum(*args):
    """
    Суммирует числа из:
    1) вложенных списков ([[1, 2], [3, [4]]])
    2) набора параметров (1, 2, 3, 4, 5)
    3) комбинации обоих вариантов
    """
    # Если передан один аргумент и это список/кортеж, обрабатываем его содержимое
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        items = flatten(args[0])
    else:
        # Иначе обрабатываем все аргументы как отдельные элементы
        items = flatten(args)

    # Суммируем все числовые элементы
    total = 0
    for item in items:
        if isinstance(item, (int, float)):
            total += item
        # Можно добавить обработку других типов, если нужно:
        # elif isinstance(item, (complex, decimal.Decimal)):
        #     total += item
    return total


# Примеры использования (для тестирования):
if __name__ == "__main__":
    # Тест 1: Вложенные списки
    print(custom_sum([[1, 2, [3]], [1], 3]))  # Ожидаемый результат: 10

    # Тест 2: Набор параметров
    print(custom_sum(1, 2, 3, 4, 5))  # Ожидаемый результат: 15

    # Тест 3: Комбинация
    print(custom_sum([1, 2], 3, [4, [5]]))  # Ожидаемый результат: 15

    # Тест 4: Один плоский список
    print(custom_sum([1, 2, 3, 4]))  # Ожидаемый результат: 10

    # Тест 5: Пустой ввод
    print(custom_sum())  # Ожидаемый результат: 0
    print(custom_sum([]))  # Ожидаемый результат: 0