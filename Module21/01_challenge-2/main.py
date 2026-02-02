# Вариант 1: Рекурсия (прямой порядок)

def without_a_cycle(num):
    if num > 0:
        without_a_cycle(num-1)
        print(num)


number = int(input('Введите число: '))
without_a_cycle(number)


# Вариант 2: Рекурсия с одним аргументом python

def print_numbers(num):
    if num > 1:
        print_numbers(num - 1)
    print(num)


# Вариант 3: Использование range и map python

def print_numbers(num):
    list(map(print, range(1, num + 1)))

print_numbers(10)


# Вариант 4: Использование * оператора распаковки python

def print_numbers(num):
    print(*range(1, num + 1), sep='\n')

print_numbers(10)


# Вариант 5: Генератор списка (технически без явного цикла for/while ) python

def print_numbers(num):
    [print(i) for i in range(1, num + 1)]

print_numbers(10)


# Вариант 6: Рекурсия с аккумулятором python

def print_numbers(num, current=1):
    if current <= num:
        print(current)
        print_numbers(num, current + 1)

print_numbers(10)

