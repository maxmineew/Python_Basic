import random

def generate_random_list(count = 10):
    random_list = [random.randint(0, 99) for _ in range(count)]
    return random_list

def create_pairs(original_list):
    paired_list = [(original_list[i], original_list[i+1]) for i in range(0, len(original_list), 2) if i + 1 < len(original_list)]
    return paired_list


random_list  = generate_random_list()
print("Оригинальный список:", random_list)

paired_list = create_pairs(random_list)
print("Новый список:", paired_list)