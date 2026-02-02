year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))
print(f'\nГоды от {year_1} до {year_2} с тремя одинаковыми цифрами:')

for year in range(year_1, year_2 + 1):
    year_str = str(year)

    digit_count = {}
    for digit in year_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    has_three_equal_digits = False
    for count in digit_count.values():
        if count == 3:
            has_three_equal_digits = True
            break

    if has_three_equal_digits:
        print(year)
