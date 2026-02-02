import os


def get_directory_stats(path):
    """Рекурсивно подсчитывает количество файлов, подкаталогов и общий размер каталога"""
    total_files = 0
    total_dirs = 0
    total_size = 0

    try:
        # Рекурсивный обход каталога
        for root, dirs, files in os.walk(path):
            total_files += len(files)
            total_dirs += len(dirs)

            # Суммируем размеры файлов в текущем каталоге
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, PermissionError):
                    # Если нет доступа к файлу, пропускаем его
                    continue

        # Преобразуем размер в килобайты (1 КБ = 1024 байта)
        size_kb = total_size / 1024

        return total_files, total_dirs, size_kb

    except (FileNotFoundError, PermissionError) as e:
        print(f"Ошибка доступа к каталогу: {e}")
        return None


def main():
    # Получаем путь от пользователя
    path = input("Введите путь до каталога: ").strip()

    # Если путь пустой, используем текущий каталог
    if not path:
        path = "."

    # Проверяем, существует ли путь
    if not os.path.exists(path):
        print("Ошибка: указанный путь не существует.")
        return

    # Проверяем, является ли путь каталогом
    if not os.path.isdir(path):
        print("Ошибка: указанный путь не является каталогом.")
        return

    # Получаем статистику каталога
    stats = get_directory_stats(path)

    if stats is not None:
        total_files, total_dirs, size_kb = stats

        print("\n" + "=" * 50)
        print(f"Статистика каталога: {os.path.abspath(path)}")
        print("=" * 50)
        print(f"Всего файлов: {total_files}")
        print(f"Всего подкаталогов: {total_dirs}")
        print(f"Общий размер: {size_kb:.2f} КБ ({size_kb * 1024:.0f} байт)")
        print("=" * 50)


if __name__ == "__main__":
    main()