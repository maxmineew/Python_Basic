import zipfile
import os
from collections import Counter
import sys


def extract_zip(zip_path, extract_to='.'):
    """Распаковывает архив с романом."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Находим файл с романом (предполагаем, что он там один)
            files = zip_ref.namelist()
            print(f"Найдены файлы в архиве: {files}")

            # Ищем текстовый файл (может быть .txt или без расширения)
            text_file = None
            for file in files:
                if 'война' in file.lower() or 'voina' in file.lower() or file.endswith('.txt'):
                    text_file = file
                    break

            if not text_file and files:
                text_file = files[0]  # берем первый файл, если не нашли по названию

            if not text_file:
                raise FileNotFoundError("В архиве не найден текстовый файл")

            print(f"Используем файл: {text_file}")

            # Распаковываем файл
            zip_ref.extract(text_file, extract_to)
            return os.path.join(extract_to, text_file)

    except FileNotFoundError:
        print(f"Ошибка: архив {zip_path} не найден!")
        sys.exit(1)
    except zipfile.BadZipFile:
        print(f"Ошибка: {zip_path} не является корректным ZIP-архивом!")
        sys.exit(1)


def count_letters(file_path):
    """Подсчитывает статистику по буквам в файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Подсчитываем только буквы (используем isalpha() для проверки)
        # Регистр учитывается, так как мы не приводим к одному регистру
        letter_counter = Counter()

        for char in text:
            if char.isalpha():  # проверяем, является ли символ буквой
                letter_counter[char] += 1

        return letter_counter

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден!")
        sys.exit(1)
    except UnicodeDecodeError:
        # Пробуем другие кодировки, если utf-8 не сработала
        encodings = ['cp1251', 'koi8-r', 'iso-8859-5', 'maccyrillic']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    text = file.read()

                letter_counter = Counter()
                for char in text:
                    if char.isalpha():
                        letter_counter[char] += 1
                return letter_counter

            except UnicodeDecodeError:
                continue

        print(f"Ошибка: не удалось прочитать файл {file_path} в известных кодировках!")
        sys.exit(1)


def save_statistics(statistics, output_file=None, sort_desc=True):
    """Сохраняет статистику в файл или выводит на экран."""
    # Сортируем по частоте
    sorted_stats = sorted(statistics.items(), key=lambda x: x[1], reverse=sort_desc)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Статистика по буквам в романе 'Война и мир':\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Буква':<10} {'Частота':<10} {'Процент':<10}\n")
            f.write("-" * 50 + "\n")

            total_chars = sum(statistics.values())
            for char, count in sorted_stats:
                percentage = (count / total_chars) * 100
                # Для специальных символов используем repr
                f.write(f"{repr(char)[1:-1]:<10} {count:<10} {percentage:.2f}%\n")

        print(f"Результат сохранен в файл: {output_file}")
    else:
        # Выводим на экран
        print("\nСтатистика по буквам в романе 'Война и мир':")
        print("=" * 60)
        print(f"{'Буква':<10} {'Частота':<10} {'Процент':<10}")
        print("-" * 60)

        total_chars = sum(statistics.values())
        for char, count in sorted_stats:
            percentage = (count / total_chars) * 100
            # Для специальных символов используем repr
            print(f"{repr(char)[1:-1]:<10} {count:<10} {percentage:.2f}%")


def main():
    # Путь к архиву (предполагаем, что он в той же директории)
    zip_file = "voina-i-mir.zip"

    # Распаковываем архив
    print("Распаковываем архив...")
    extracted_file = extract_zip(zip_file)
    print(f"Файл распакован: {extracted_file}")

    # Подсчитываем статистику
    print("Подсчитываем статистику по буквам...")
    stats = count_letters(extracted_file)

    # Выводим результаты
    print(f"\nВсего найдено {len(stats)} уникальных букв")
    print(f"Всего букв в тексте: {sum(stats.values())}")

    # Сохраняем в файл и выводим на экран топ-20
    save_statistics(stats, output_file="letter_statistics.txt", sort_desc=True)

    # Также выводим топ-20 на экран для быстрого просмотра
    print("\nТоп-20 самых частых букв:")
    print("=" * 40)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    for i, (char, count) in enumerate(sorted_stats[:20], 1):
        percentage = (count / sum(stats.values())) * 100
        print(f"{i:2}. {repr(char)[1:-1]:<5} - {count:8} раз ({percentage:.2f}%)")

    # Удаляем распакованный файл (опционально)
    try:
        os.remove(extracted_file)
        print(f"\nВременный файл {extracted_file} удален")
    except:
        pass


if __name__ == "__main__":
    main()