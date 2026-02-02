video_cards = []

num_cards = int(input('Количество видеокарт:'))

for i in range(1, num_cards + 1):
    num = int(input(f'Видеокарта {i}: '))
    video_cards.append(num)
print()
print(f'Старый список видео карт {video_cards}')

max_value = max(video_cards)
while max_value in video_cards:
    video_cards.remove(max_value)

print(f'Новый список видеокарт: {video_cards}')


