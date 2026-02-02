def del1(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i


digit = int(input("Введите число: "))
print(f"Наименьший делитель, отличный от единицы: {del1(digit)}")
