students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']  # Исправлено: теперь список
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def extract_student_info(students_dict):
    """Извлекает информацию о студентах: уникальные интересы и общую длину фамилий."""
    # Используем set comprehension для уникальных интересов
    unique_interests = {
        interest
        for student in students_dict.values()
        for interest in student['interests']
    }

    # Суммируем длины всех фамилий
    total_surname_length = sum(len(student['surname'])
                               for student in students_dict.values())

    return unique_interests, total_surname_length


# Создаем список пар (ID, возраст) с использованием list comprehension
id_age_pairs = [(student_id, info['age'])
                for student_id, info in students.items()]

# Получаем результаты из функции
interests, surname_length = extract_student_info(students)

print(f"Уникальные интересы студентов: {interests}")
print(f"Общая длина всех фамилий: {surname_length}")
print(f"Пары (ID студента, возраст): {id_age_pairs}")

# Дополнительно: вывод для проверки
print(f"\nОбщее количество уникальных интересов: {len(interests)}")
print(f"Список пар в читаемом виде:")
for student_id, age in id_age_pairs:
    print(f"  Студент {student_id}: {students[student_id]['name']} {students[student_id]['surname']}, возраст: {age}")