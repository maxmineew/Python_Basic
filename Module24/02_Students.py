class Student:
    """Класс для представления студента"""

    def __init__(self, full_name, group_number, grades):
        """
        Инициализация студента

        Args:
            full_name (str): Фамилия Имя Отчество
            group_number (str): Номер группы
            grades (list): Список из 5 оценок
        """
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades
        self.average_score = self.calculate_average()

    def calculate_average(self):
        """Вычисляет средний балл студента"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """Строковое представление студента"""
        return (f"Студент: {self.full_name:<20} "
                f"Группа: {self.group_number:<8} "
                f"Оценки: {self.grades} "
                f"Средний балл: {self.average_score:.2f}")

    def __repr__(self):
        """Для отладки"""
        return f"Student('{self.full_name}', '{self.group_number}', {self.grades})"


def input_student_data():
    """Запрашивает данные о студенте у пользователя"""
    print("\n" + "=" * 50)
    print("Введите данные студента:")

    # Ввод ФИО
    while True:
        full_name = input("Фамилия Имя Отчество: ").strip()
        if full_name:
            break
        print("❌ Ошибка: ФИО не может быть пустым!")

    # Ввод номера группы
    while True:
        group_number = input("Номер группы: ").strip()
        if group_number:
            break
        print("❌ Ошибка: Номер группы не может быть пустым!")

    # Ввод 5 оценок
    grades = []
    print("Введите 5 оценок (от 1 до 5):")

    for i in range(1, 6):
        while True:
            try:
                grade = int(input(f"Оценка {i}: "))
                if 1 <= grade <= 5:
                    grades.append(grade)
                    break
                else:
                    print("❌ Ошибка: Оценка должна быть от 1 до 5!")
            except ValueError:
                print("❌ Ошибка: Введите целое число!")

    return Student(full_name, group_number, grades)


def create_students_list():
    """Создает список студентов"""
    students = []

    print("=" * 60)
    print("ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ УЧЕТА СТУДЕНТОВ")
    print("=" * 60)

    # Запрашиваем количество студентов
    while True:
        try:
            num_students = int(input(
                "Сколько студентов вы хотите добавить? (рекомендуется 10): "))
            if num_students > 0:
                break
            else:
                print("❌ Ошибка: Число должно быть положительным!")
        except ValueError:
            print("❌ Ошибка: Введите целое число!")

    # Запрашиваем данные для каждого студента
    for i in range(num_students):
        print(f"\n📝 Добавление студента {i + 1} из {num_students}")
        student = input_student_data()
        students.append(student)
        print(f"✅ Студент '{student.full_name}' успешно добавлен!")

    return students


def sort_students_by_average(students):
    """Сортирует студентов по среднему баллу (по возрастанию)"""
    return sorted(students, key=lambda student: student.average_score)


def sort_students_by_average_desc(students):
    """Сортирует студентов по среднему баллу (по убыванию)"""
    return sorted(students, key=lambda student: student.average_score,
                  reverse=True)


def display_students(students, title="СПИСОК СТУДЕНТОВ"):
    """Отображает список студентов"""
    print("\n" + "=" * 80)
    print(f"{title.upper()}")
    print("=" * 80)

    if not students:
        print("Список студентов пуст.")
        return

    print(
        f"{'№':<4} {'ФИО':<25} {'Группа':<10} {'Оценки':<15} {'Средний балл':<12} {'Статус':<10}")
    print("-" * 80)

    for idx, student in enumerate(students, 1):
        # Определяем статус студента по среднему баллу
        if student.average_score >= 4.5:
            status = "Отличник"
        elif student.average_score >= 3.5:
            status = "Хорошист"
        elif student.average_score >= 2.5:
            status = "Удовлет."
        else:
            status = "Неуспева."

        print(f"{idx:<4} "
              f"{student.full_name:<25} "
              f"{student.group_number:<10} "
              f"{str(student.grades):<15} "
              f"{student.average_score:<12.2f} "
              f"{status:<10}")


def show_statistics(students):
    """Показывает статистику по студентам"""
    if not students:
        print("Нет данных для статистики.")
        return

    print("\n" + "=" * 50)
    print("СТАТИСТИКА")
    print("=" * 50)

    # Вычисляем общую статистику
    total_students = len(students)
    average_scores = [s.average_score for s in students]

    print(f"Всего студентов: {total_students}")
    print(
        f"Средний балл по группе: {sum(average_scores) / total_students:.2f}")
    print(f"Максимальный средний балл: {max(average_scores):.2f}")
    print(f"Минимальный средний балл: {min(average_scores):.2f}")

    # Статистика по успеваемости
    excellent = len([s for s in students if s.average_score >= 4.5])
    good = len([s for s in students if 3.5 <= s.average_score < 4.5])
    satisfactory = len([s for s in students if 2.5 <= s.average_score < 3.5])
    unsatisfactory = len([s for s in students if s.average_score < 2.5])

    print(
        f"\nОтличники (≥4.5): {excellent} ({excellent / total_students * 100:.1f}%)")
    print(f"Хорошисты (3.5-4.5): {good} ({good / total_students * 100:.1f}%)")
    print(
        f"Удовлетворительно (2.5-3.5): {satisfactory} ({satisfactory / total_students * 100:.1f}%)")
    print(
        f"Неуспевающие (<2.5): {unsatisfactory} ({unsatisfactory / total_students * 100:.1f}%)")


def demo_mode():
    """Режим демонстрации с готовыми данными"""
    print("\n" + "=" * 60)
    print("РЕЖИМ ДЕМОНСТРАЦИИ")
    print("Используются предустановленные данные")
    print("=" * 60)

    # Создаем 10 студентов с готовыми данными
    demo_students = [
        Student("Иванов Иван Иванович", "ГР-101", [5, 4, 5, 5, 4]),
        Student("Петров Петр Петрович", "ГР-101", [3, 3, 4, 3, 4]),
        Student("Сидорова Анна Сергеевна", "ГР-102", [5, 5, 5, 5, 5]),
        Student("Козлов Алексей Дмитриевич", "ГР-103", [2, 3, 2, 3, 2]),
        Student("Смирнова Мария Игоревна", "ГР-102", [4, 4, 5, 4, 4]),
        Student("Васильев Дмитрий Алексеевич", "ГР-101", [3, 4, 3, 3, 4]),
        Student("Николаева Екатерина Валерьевна", "ГР-103", [5, 4, 5, 4, 5]),
        Student("Алексеев Андрей Сергеевич", "ГР-102", [4, 3, 4, 4, 3]),
        Student("Федорова Ольга Петровна", "ГР-101", [2, 2, 3, 2, 3]),
        Student("Дмитриев Сергей Викторович", "ГР-103", [4, 5, 4, 5, 4])
    ]

    return demo_students


def main():
    """Основная функция программы"""
    print("🎓 СИСТЕМА УЧЕТА УСПЕВАЕМОСТИ СТУДЕНТОВ 🎓")
    print("=" * 60)

    while True:
        print("\nВыберите режим работы:")
        print("1. Ручной ввод данных студентов")
        print("2. Демонстрационный режим (10 готовых студентов)")
        print("3. Выход из программы")

        choice = input("Ваш выбор (1-3): ").strip()

        if choice == "1":
            students = create_students_list()
            break
        elif choice == "2":
            students = demo_mode()
            break
        elif choice == "3":
            print("До свидания!")
            return
        else:
            print("❌ Ошибка: Выберите 1, 2 или 3!")

    if not students:
        print("Нет данных для обработки.")
        return

    # Показываем исходный список
    display_students(students, "Исходный список студентов")

    # Сортируем по возрастанию среднего балла
    sorted_students = sort_students_by_average(students)
    display_students(sorted_students,
                     "Список студентов отсортированный по возрастанию среднего балла")

    # Сортируем по убыванию среднего балла (дополнительно)
    sorted_desc_students = sort_students_by_average_desc(students)
    display_students(sorted_desc_students,
                     "Список студентов отсортированный по убыванию среднего балла")

    # Показываем статистику
    show_statistics(students)

    # Дополнительная информация
    print("\n" + "=" * 60)
    print("ЛУЧШИЕ СТУДЕНТЫ (ТОП-3):")
    print("=" * 60)

    top_students = sorted_desc_students[:3]
    for idx, student in enumerate(top_students, 1):
        print(
            f"{idx}. {student.full_name} - средний балл: {student.average_score:.2f}")

    print("\n" + "=" * 60)
    print("ПРОГРАММА ЗАВЕРШЕНА УСПЕШНО!")
    print("=" * 60)


if __name__ == "__main__":
    main()