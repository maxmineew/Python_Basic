def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return "Адрес - это четыре числа, разделённые точками"

    for part in parts:
        if not part.isdigit():
            return f"{part} - не целое число"

        num = int(part)

        if num < 0 or num > 255:
            return f"{num} превышает 255"

    return "IP-адрес корректен"


user_input = input("Введите IP: ")
result = is_valid_ip(user_input)
print(result)
