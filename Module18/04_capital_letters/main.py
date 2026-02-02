def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

user_input = input("Введите строку: ")
result = capitalize_words(user_input)

print("Результат:", result)
