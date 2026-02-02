import re
from collections import Counter

# Чтение всего файла
with open("text.txt", "r") as file:
    text = file.read()
    print(f'Содержимое файла text.txt: \n{text}')

# Извлечение английских букв и приведение к нижнему регистру
english_letters = re.findall(r'[a-zA-Z]', text.lower())

# Подсчет общей суммы букв и частот
total_letters = len(english_letters)
letter_counts = Counter(english_letters)

# Подготовка данных для сортировки
letters_data = []
for letter, count in letter_counts.items():
    proportion = count / total_letters
    letters_data.append((letter, proportion))

# Сортировка: сначала по убыванию доли, затем по алфавиту
letters_data.sort(key=lambda x: (-x[1], x[0]))

# Запись результатов в файл
with open("analysis.txt", "w") as output_file:
    for letter, proportion in letters_data:
        output_file.write(f"{letter} {proportion:.3f}\n")

# Вывод для проверки (можно удалить)
print("Содержимое файла analysis.txt:")
for letter, proportion in letters_data:
    print(f"{letter} {proportion:.3f}")