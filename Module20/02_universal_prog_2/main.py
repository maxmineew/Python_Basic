# TODO здесь писать код
'''В задании "Для проверки на простое число напишите
отдельную функцию is_prime." -
функция должна проверять одно число на простое.
Используя эту функцию "Напишите функцию, возвращающую
список элементов итерируемого объекта "'''

def is_prime(data):
    """Проверяет, является ли число простым."""
    if data < 2:
       return False
    for index in range(2, int(data**0.5) + 1):
        if data % index == 0:
            return False
    return True

def crypto(data):
    """Возвращает список элементов с простыми индексами."""
    return [elem for index, elem in enumerate(data) if is_prime(index)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
