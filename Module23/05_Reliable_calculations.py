import math
try:
    function = input('Введите число: ')
    function_answer = math.sqrt(int(function))
    print(f'Квадратный корень числа {function} равен {function_answer}')
except ValueError:
    print('Невозможно преобразовать строку в число')
except TypeError:
    print('Функция вызвана без обязательных аргументов')
except NameError:
    print('Переменная не определена')
except FileNotFoundError:
    print('Файл не найден')
except ZeroDivisionError:
    print('Попытка выполнить деление, где делитель равен 0')
except Exception as exc:
    print(f'Ошибка: {exc}')
