# TODO здесь писать код
text = str(input('Введите текст: '))

vowels = [ i_letter for i_letter in text if i_letter in 'АОУЫЭЕЁИЮаоуыэеёию']

print('Список гласных букв:', vowels)
print('Длина списка:', len(vowels))
