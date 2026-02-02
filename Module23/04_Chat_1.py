from pyexpat.errors import messages

user_name = input('Как Вас зовут: ')
while True:
    print('Чтобы увидеть текущий текст чата введите 1, чтобы написать соообщение введите 2')
    response = input('Введите 1 или 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r', encoding = 'utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение:')
        with open('chat.txt', 'a', encoding = 'utf-8') as file:
            file.write('{name}: {message}\n'.format(name=user_name, message=new_message))
    else:
        print('Неизвестная команда\n')