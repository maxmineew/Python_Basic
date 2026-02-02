# TODO здесь писать код
h_list = str(input('Введите строку:'))

sequence = []

first_h_list_index = h_list.find('h')
last_h_list_index = h_list.rfind('h')

sequence = h_list[first_h_list_index + 1:last_h_list_index][::-1]

print('Развернутая последовательность между первым и и последним h:', sequence)
