# TODO здесь писать код

def bubble_sort(list_of_numbers):
    list_num = len(list_of_numbers)
    for i in range(list_num):
        for j in range(0, list_num-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]

list_of_numbers = [1, 4, -3, 0, 10]
print("Изначальный список:", list_of_numbers)

bubble_sort(list_of_numbers)

print("Отсортированный список:", list_of_numbers)