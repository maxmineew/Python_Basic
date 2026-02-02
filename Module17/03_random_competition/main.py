# TODO здесь писать код
import random

first_cmd = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_cmd = [round(random.uniform(5, 10), 2) for _ in range(20)]

print('Первая команда:', first_cmd)
print('Вторая команда:', second_cmd)

third_cmd = [max(i_win) for (i_win) in zip(first_cmd, second_cmd)]

print('Победители тура:', third_cmd)
