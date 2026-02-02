# Чтение данных из файла
with open("first_tour.txt", "r", encoding="utf8") as file:
    data = file.readlines()

# Получаем минимальный проходной балл K
k = int(data[0].strip())

# Обрабатываем данные участников
participants = []
for line in data[1:]:
    if line.strip():  # Пропускаем пустые строки
        surname, name, score = line.strip().split()
        score = int(score)
        if score > k:  # Проверяем, прошел ли участник во второй тур
            # Формируем запись: (баллы, фамилия, имя для сортировки)
            participants.append((score, surname, name))

# Сортируем по убыванию баллов
participants.sort(reverse=True)

# Записываем результат во второй файл
with open("second_tour.txt", "w", encoding="utf8") as file:
    # Записываем количество прошедших участников
    file.write(f"{len(participants)}\n")

    # Записываем пронумерованный список участников
    for i, (score, surname, name) in enumerate(participants, 1):
        # Получаем первую букву имени
        initial = name[0].upper()
        # Формируем строку в нужном формате
        file.write(f"{i}) {initial}. {surname} {score}\n")

# Выводим результат на экран для проверки
print("Содержимое файла first_tour.txt:")
with open("first_tour.txt", "r", encoding="utf8") as file:
    print(file.read())

print("\nСодержимое файла second_tour.txt:")
with open("second_tour.txt", "r", encoding="utf8") as file:
    print(file.read())