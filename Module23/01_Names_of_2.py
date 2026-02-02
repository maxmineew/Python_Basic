try:
    with open('people.txt', 'r', encoding='utf-8') as people_file:
        lines = people_file.readlines()

    with open('errors.log', 'w', encoding='utf-8') as log_file:
        line_count = 0
        sym_sum = 0
        removed_count = 0

        for i, line in enumerate(lines, 1):
            line = line.rstrip('\n')  # Убираем символ новой строки

            if not line.strip():  # Если строка пустая или содержит только пробелы
                removed_count += 1
                continue

            line_count += 1
            line_length = len(line)
            sym_sum += line_length

            if line_length < 3:
                error_message = f'Ошибка: менее трёх символов в строке {line_count}.'
                log_file.write(error_message + '\n')
                print(error_message)

    print(f'Обработано строк: {line_count}')
    print(f'Удалено пустых строк: {removed_count}')
    print(f'Общее количество символов: {sym_sum}')

except FileNotFoundError:
    print("Файл 'people.txt' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")