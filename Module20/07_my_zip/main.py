# TODO здесь писать код
def my_zip(*iterables):
    min_length = min(len(iterable) for iterable in iterables)
    return (
        tuple(iterable[i] for iterable in iterables)
        for i in range(min_length)
    )


my_string = "abcd"
my_tuple = (10, 20, 30, 40)
print(f"Исходная строка: {my_string}")
print(f"Исходный кортеж чисел: {my_tuple}")

my_zip_generator = my_zip(my_string, my_tuple)
print("\nСозданный генератор:", my_zip_generator)
print("\nСгенерированные кортежи:")

for pair in my_zip_generator:
    print(pair)