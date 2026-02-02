main_list = [1, 5, 3]
first_list= [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_list)
decode_1 = main_list.count(5)

print('Результат работы программы:')
print(f'\nКол-во цифр 5 при первом объединении: {decode_1}')

while 5 in main_list:
    main_list.remove(5)
    
main_list.extend(second_list)
decode_2 = main_list.count(3)

print(f'\nКол-во цифр 3 при втором объединении: {decode_2}')
print(f'\nИтоговый список: {main_list}')
