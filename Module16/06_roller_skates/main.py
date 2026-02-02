def max_people_with_skates(skates, feet):
    skates.sort()
    feet.sort()
    
    max_people = 0
    i = 0
    j = 0
    
    while i < len(skates) and j < len(feet):
        if skates[i] == feet[j]:
            max_people += 1
            i += 1
            j += 1
        elif skates[i] < feet[j]:
            i += 1
        else:
            j += 1
    
    return max_people

num_roule = int(input('Кол-во коньков: '))
skates = []
for num in range(num_roule):
    size = int(input(f'Размер {num + 1}-й пары: '))
    skates.append(size)
print()

num_people = int(input('Кол-во людей: '))
feet = []
for numb in range(num_people):
    size = int(input(f'Размер ноги {numb + 1}-го человека: '))
    feet.append(size)

result = max_people_with_skates(skates, feet)
print(f"Наибольшее кол-во людей, которые могут взять ролики: {result}")
