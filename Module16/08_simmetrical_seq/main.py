def palindrome(simmetric_list):
    reverse_list = []
    for i_num in range(len(simmetric_list) - 1, -1, -1):
        reverse_list.append(simmetric_list[i_num])
    if simmetric_list == reverse_list:
        return True
    else:
         return False

numbers = int(input('Количество чисел:'))
sequence_list = []
num_list = []
first_list = []

for num in range(1, numbers + 1):
   sequence = int(input(f' Число: '))
   sequence_list.append(sequence)
print(f'Последовательность: {sequence_list}')
    
for i in range(0, len(sequence_list)):
    for j in range(i, len(sequence_list)):
        num_list.append(sequence_list[j])
    if palindrome(num_list):
        for i_ans in range(0, i):
            first_list.append(sequence_list[i_ans])
        first_list.reverse()
        break
    num_list = []

print(f'Нужно приписать чисел: {len(first_list)}')
print(f'Сами числа: {first_list}')
