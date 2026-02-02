string = max(input('Введите строку: ').split(), key = len)

print('Самое длинное слово:', string, '\nДлина этого слова: ', len(string))