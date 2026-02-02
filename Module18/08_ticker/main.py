def is_cyclic_shift(str1, str2):
    if len(str1) != len(str2):
        return False, -1

    doubled_str2 = str2 + str2

    index = doubled_str2.find(str1)

    if index != -1:
        return True, index
    else:
        return False, -1


str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

result, shift = is_cyclic_shift(str1, str2)

if result:
    print(f"Первая строка получается из второй со сдвигом {shift}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
