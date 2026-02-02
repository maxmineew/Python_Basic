num = int(input('Введите число:'))

numbers = []

for i in range(1, num, 2):
    numbers.append(i)

print(f'Список из нечётных чисел от одного до N: {numbers}')
