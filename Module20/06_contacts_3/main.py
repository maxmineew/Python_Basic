# TODO здесь писать код
def add_contact(contacts):
    name_surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
    if len(name_surname) != 2:
        print("Некорректный ввод. Введите имя и фамилию через пробел.")
        return contacts
    name, surname = name_surname
    contact_key = (name, surname)
    if contact_key in contacts:
        print("Такой человек уже есть в контактах.")
    else:
        phone = input("Введите номер телефона: ")
        contacts[contact_key] = phone
    print("Текущий словарь контактов:", contacts)
    return contacts

def find_contact(contacts):
    surname = input("Введите фамилию для поиска: ").lower()
    found = False
    for (name, s_name), phone in contacts.items():
        if s_name.lower() == surname:
            print(name, s_name, phone)
            found = True
    if not found:
        print("Контакты с такой фамилией не найдены.")

def main():
    contacts = {}
    while True:
        print("Введите номер действия:")
        print(" 1. Добавить контакт")
        print(" 2. Найти человека")
        action = input().strip()
        if action == '1':
            contacts = add_contact(contacts)
        elif action == '2':
            find_contact(contacts)
        else:
            print("Некорректный ввод. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
    main()