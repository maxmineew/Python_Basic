def find_last_person(num_people, num):
    people = list(range(1, num_people + 1))
    index = 0

    while len(people) > 1:
        index = (index + num - 1) % len(people)
        print(f'Текущий круг людей: {people}')
        print(f'Начало счета с номера {people[index]}')
        print(f'Выбывает человек под номером {people.pop(index)}')
        print()

    return people[0]

num_people = int(input("Кол-во человек: "))
num = int(input("Какое число в считалке? "))
print(f'Значит выбывает каждый {num}-й человек')
print()

result = find_last_person(num_people, num)
print(f"Остался человек под номером {result}")
