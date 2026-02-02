# TODO здесь писать код

def weight_check(weight):
    while weight > 200:
        print(f'Вес контейнера превышает максимальный вес в 200 кг!')
        weight = int(input(f'Введите вес контейнера еще раз: '))
    return weight


num = int(input("Количество контейнеров: "))
containers = []
for _ in range(num):
    container_weight = int(input(f"Введите вес контейнера: "))
    check1 = weight_check(container_weight)
    containers.append(check1)
    # print(containers)

new_containers = int(input("Введите вес нового контейнера: "))
check2 = weight_check(new_containers)
count = 1
for cont in containers:
    if new_containers <= cont:
        count += 1
    else:
        break

print("Номер, который получит новый контейнер:", count)