import copy


def deep_copy_and_replace(site_template, product_name):
    """Создает глубокую копию сайта и заменяет название продукта"""
    # Создаем глубокую копию сайта
    site_copy = copy.deepcopy(site_template)

    # Рекурсивная функция для поиска и замены значений
    def replace_value(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    # Заменяем слово 'телефон' на название продукта
                    if 'телефон' in value.lower():
                        data[key] = value.replace('телефон', product_name)
                    # Заменяем 'iPhone' на название продукта
                    elif 'iPhone' in value:
                        data[key] = value.replace('iPhone', product_name)
                elif isinstance(value, dict):
                    replace_value(value)

    replace_value(site_copy)
    return site_copy


def print_site(site_dict, product_name):
    """Выводит структуру сайта в нужном формате"""
    print(f"Сайт для {product_name}:")
    print("site = {", end="")
    _print_dict_recursive(site_dict, 1)
    print("}")


def _print_dict_recursive(data, indent_level):
    """Рекурсивно выводит словарь с отступами"""
    indent = "  " * indent_level
    items = list(data.items())

    for i, (key, value) in enumerate(items):
        if isinstance(value, dict):
            print(f"\n{indent}'{key}': {{", end="")
            _print_dict_recursive(value, indent_level + 1)
            if i == len(items) - 1:
                print(f"\n{indent}}}", end="")
            else:
                print(f"\n{indent}}},", end="")
        else:
            if i == len(items) - 1:
                print(f"\n{indent}'{key}': '{value}'", end="")
            else:
                print(f"\n{indent}'{key}': '{value}',", end="")


def main():
    """Основная функция программы"""
    # Исходный шаблон сайта
    site_template = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iPhone',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    # Запрашиваем количество сайтов
    try:
        num_sites = int(input("Сколько сайтов: "))
    except ValueError:
        print("Ошибка: введите число!")
        return

    # Список для хранения всех сайтов
    all_sites = []

    # Создаем сайты для каждого продукта
    for _ in range(num_sites):
        product_name = input("\nВведите название продукта для нового сайта: ")

        # Создаем глубокую копию и заменяем названия
        new_site = deep_copy_and_replace(site_template, product_name)
        all_sites.append((product_name, new_site))

        # Выводим все созданные сайты
        print()
        for product, site in all_sites:
            print_site(site, product)
            print()


if __name__ == "__main__":
    main()