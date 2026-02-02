films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код

favorite_films = []

num_films = int(input('Сколько фильмов хотите добавить? '))

for _ in range(num_films):
    film = input('Введите название фильма: ')
    if film in films:
        favorite_films.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print(f'Ваш список любимых фильмов:', ', '.join(favorite_films))