def partition(nums):
    """
    Вспомогательная функция для разделения списка на три части:
    элементы меньше опорного, равные опорному и больше опорного.
    Опорный элемент - последний элемент списка.

    Args:
        nums (list): Исходный список для разделения

    Returns:
        tuple: Три списка (меньшие, равные, большие)
    """
    if not nums:
        return [], [], []

    pivot = nums[-1]  # Опорный элемент - крайний правый
    '''
    Мы используем nums[-1], потому что в условии задачи сказано: 
"опорным элементом всегда будет крайний правый (например, в списке [1, 2, 3] это 3)."
В Python отрицательные индексы позволяют обращаться к элементам с конца списка:
nums[-1] - последний элемент,
nums[-2] - предпоследний и так далее.
   Таким образом, nums[-1] - это компактный и понятный способ выбрать 
последний элемент списка в качестве опорного.
    '''
    less = []
    equal = []
    greater = []

    for num in nums:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return less, equal, greater


def quick_sort(nums):
    """
    Основная функция быстрой сортировки (сортировки Хоара).
    Рекурсивно сортирует список по возрастанию.

    Args:
        nums (list): Исходный список для сортировки

    Returns:
        list: Отсортированный список
    """
    # Базовый случай рекурсии: список из 0 или 1 элемента уже отсортирован
    if len(nums) <= 1:
        return nums

    # Разделяем список на три части
    less, equal, greater = partition(nums)

    # Рекурсивно сортируем части с меньшими и большими элементами
    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)

    # Объединяем отсортированные части
    return sorted_less + equal + sorted_greater


def main():
    """Основная функция для демонстрации работы алгоритма"""
    # Тестовые примеры из задания
    test_cases = [
        [5, 8, 9, 4, 2, 9, 1, 8],
        [4, 9, 2, 7, 5],
        [1, 2, 3],
        [9, 9],
        [5, 4, 2, 1],
        []
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"Тест {i}:")
        print(f"  Исходный список: {test_case}")

        # Демонстрация работы вспомогательной функции
        less, equal, greater = partition(test_case)
        print(f"  Результат partition: меньше {less}, равны {equal}, больше {greater}")

        # Сортировка
        sorted_list = quick_sort(test_case)
        print(f"  Отсортированный список: {sorted_list}")
        print()


if __name__ == "__main__":
    main()