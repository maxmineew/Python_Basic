def check_file_name(file_name):
    special_characters = '@№$%^&*()'

    if file_name.startswith(tuple(special_characters)):
        return "Ошибка: название начинается на один из специальных символов."

    if not (file_name.endswith('.txt') or file_name.endswith('.docx')):
        return "Ошибка: неверное расширение файла. Ожидалось .txt или .docx."

    return "Файл назван верно."

file_name_input = input("Название файла: ")
result = check_file_name(file_name_input)

print(result)