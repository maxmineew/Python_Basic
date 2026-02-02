# TODO здесь писать код
num_list = int(input('Введите длину списка:'))

answer = [1 if i_num % 2 == 0 else i_num % 5
for i_num in range(num_list)]

print('Результат', answer)
