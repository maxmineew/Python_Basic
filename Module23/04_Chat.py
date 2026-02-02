chat_history = []

while True:
    name = input('Введите имя пользователя:').strip()
    if not name:
        print('Нужно ввести имя. Попробуйте еще раз.')
        continue
    while True:
        try:
            action = input('1. Посмотреть текущий текст чата.'
                           '\n2. Ввести и отправить сообщение.'
                           '\n3. Выход из программы.'
                           '\nВыберите действие:')
            if action == '1':
                try:
                    with open('chat.txt', 'r', encoding='utf-8') as file:
                        messages = file.readlines()
                        print(''.join(messages))
                except FileNotFoundError:
                    print('Служебное сообщение: пока ничего нет\n')
            elif action == '2':
                message = input('Введите сообщение:')
                with open('chat.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{name}: {message}\n')
            elif action == '3':
                print('Выход из программы.')
                break
        except Exception as e:
            print(f'Произошла ошибка: {e}')


