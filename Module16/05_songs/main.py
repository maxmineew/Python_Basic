violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
total_time = 0
playlist = []

num_track = int(input('Сколько песен выбрать? '))

for num in range(num_track):
    track = input(f'Название {num + 1}-й песни: ')
    for number in violator_songs:
        if number[0] == track:
            playlist.append(number)
            total_time += number[1]
            break
print(f'\nОбщее время звучания пеcен: {round(total_time, 2)} минуты.')
