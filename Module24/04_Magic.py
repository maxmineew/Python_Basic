class Element:
    """Базовый класс для всех элементов"""

    def __init__(self, name="Неизвестный элемент"):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Element('{self.name}')"

    def __add__(self, other):
        # Получаем имена классов элементов
        elements_pair = (self.__class__.__name__, other.__class__.__name__)

        # Таблица преобразований (независимо от порядка)
        combinations = {
            frozenset(['Water', 'Air']): Storm,
            frozenset(['Water', 'Fire']): Steam,
            frozenset(['Water', 'Earth']): Mud,
            frozenset(['Air', 'Fire']): Lightning,
            frozenset(['Air', 'Earth']): Dust,
            frozenset(['Fire', 'Earth']): Lava,
            frozenset(['Life', 'Water']): Plant,
            frozenset(['Life', 'Earth']): Animal,
            frozenset(['Life', 'Fire']): Energy,
            frozenset(['Life', 'Air']): Spirit,
            frozenset(['Time', 'Fire']): Ash,
            frozenset(['Time', 'Water']): Ice,
            frozenset(['Time', 'Earth']): Fossil,
            frozenset(['Time', 'Air']): Void,
            frozenset(['Plant', 'Fire']): Smoke,
            frozenset(['Animal', 'Water']): Fish,
            frozenset(['Energy', 'Air']): Storm,
            frozenset(['Spirit', 'Earth']): Crystal,
            frozenset(['Ice', 'Fire']): Water,
            frozenset(['Crystal', 'Lightning']): Diamond
        }

        # Ищем комбинацию
        pair_key = frozenset(elements_pair)
        if pair_key in combinations:
            return combinations[pair_key]()
        else:
            return None


# Базовые элементы
class Water(Element):
    def __init__(self):
        super().__init__("💧 Вода")

    def __add__(self, other):
        result = super().__add__(other)
        if result:
            return result
        return None


class Air(Element):
    def __init__(self):
        super().__init__("💨 Воздух")

    def __add__(self, other):
        result = super().__add__(other)
        if result:
            return result
        return None


class Fire(Element):
    def __init__(self):
        super().__init__("🔥 Огонь")

    def __add__(self, other):
        result = super().__add__(other)
        if result:
            return result
        return None


class Earth(Element):
    def __init__(self):
        super().__init__("🌍 Земля")

    def __add__(self, other):
        result = super().__add__(other)
        if result:
            return result
        return None


# Производные элементы из условия
class Storm(Element):
    def __init__(self):
        super().__init__("⛈ Шторм")


class Steam(Element):
    def __init__(self):
        super().__init__("💨 Пар")


class Mud(Element):
    def __init__(self):
        super().__init__("🟤 Грязь")


class Lightning(Element):
    def __init__(self):
        super().__init__("⚡ Молния")


class Dust(Element):
    def __init__(self):
        super().__init__("🌫 Пыль")


class Lava(Element):
    def __init__(self):
        super().__init__("🌋 Лава")


# Собственные элементы (дополнительно)
class Life(Element):
    """Новый базовый элемент: Жизнь"""

    def __init__(self):
        super().__init__("🌱 Жизнь")


class Time(Element):
    """Новый базовый элемент: Время"""

    def __init__(self):
        super().__init__("⏳ Время")


# Производные от собственных элементов
class Plant(Element):
    def __init__(self):
        super().__init__("🌿 Растение")


class Animal(Element):
    def __init__(self):
        super().__init__("🐾 Животное")


class Energy(Element):
    def __init__(self):
        super().__init__("⚡ Энергия")


class Spirit(Element):
    def __init__(self):
        super().__init__("👻 Дух")


class Ash(Element):
    def __init__(self):
        super().__init__("🪵 Пепел")


class Ice(Element):
    def __init__(self):
        super().__init__("❄️ Лёд")


class Fossil(Element):
    def __init__(self):
        super().__init__("🦴 Ископаемое")


class Void(Element):
    def __init__(self):
        super().__init__("🌀 Пустота")


class Smoke(Element):
    def __init__(self):
        super().__init__("💨 Дым")


class Fish(Element):
    def __init__(self):
        super().__init__("🐟 Рыба")


class Crystal(Element):
    def __init__(self):
        super().__init__("💎 Кристалл")


class Diamond(Element):
    def __init__(self):
        super().__init__("💎 Алмаз")


# Вспомогательные функции
def combine_elements(element1, element2):
    """Функция для сложения элементов с красивым выводом"""
    print(f"{element1} + {element2} = ", end="")
    result = element1 + element2
    if result:
        print(f"{result}")
    else:
        print("❌ Нет результата")
    return result


def magic_cauldron():
    """Интерактивный котел для алхимии"""
    print("=" * 60)
    print("🔮 МАГИЧЕСКИЙ КОТЕЛ АЛХИМИКА")
    print("=" * 60)

    # Создаем базовые элементы
    elements = {
        '1': Water(),
        '2': Air(),
        '3': Fire(),
        '4': Earth(),
        '5': Life(),
        '6': Time()
    }

    # Показываем доступные элементы
    print("\nДоступные элементы:")
    for key, element in elements.items():
        print(f"  {key}. {element}")

    # Пользователь выбирает элементы
    print("\nВыберите два элемента для смешивания:")
    element1_key = input("Первый элемент (1-6): ")
    element2_key = input("Второй элемент (1-6): ")

    if element1_key in elements and element2_key in elements:
        result = combine_elements(elements[element1_key],
                                  elements[element2_key])

        # Если есть результат, спрашиваем, не хочет ли пользователь смешать еще
        if result:
            print("\nХотите смешать результат с другим элементом? (да/нет)")
            if input().lower() in ['да', 'yes', 'д', 'y']:
                print("\nВыберите элемент для смешивания с результатом:")
                for key, element in elements.items():
                    print(f"  {key}. {element}")

                element3_key = input("Элемент (1-6): ")
                if element3_key in elements:
                    combine_elements(result, elements[element3_key])
    else:
        print("❌ Неверный выбор элементов!")


def run_all_combinations():
    """Запуск всех возможных комбинаций"""
    print("=" * 60)
    print("🧪 ВСЕ КОМБИНАЦИИ ЭЛЕМЕНТОВ")
    print("=" * 60)

    # Базовые элементы
    water = Water()
    air = Air()
    fire = Fire()
    earth = Earth()
    life = Life()
    time = Time()

    # Все пары базовых элементов
    elements_list = [water, air, fire, earth, life, time]
    element_names = ["Вода", "Воздух", "Огонь", "Земля", "Жизнь", "Время"]

    print("\n1. Комбинации базовых элементов:")
    for i in range(len(elements_list)):
        for j in range(i + 1, len(elements_list)):
            print(f"  {element_names[i]} + {element_names[j]} = ", end="")
            result = elements_list[i] + elements_list[j]
            print(f"{result if result else 'Нет результата'}")

    # Некоторые интересные комбинации с производными элементами
    print("\n2. Расширенные комбинации:")

    # Создаем производные элементы
    storm = Storm()
    steam = Steam()
    mud = Mud()
    lightning = Lightning()
    dust = Dust()
    lava = Lava()
    plant = Plant()
    energy = Energy()

    # Показываем некоторые комбинации
    test_combinations = [
        (storm, fire, "Шторм + Огонь"),
        (steam, earth, "Пар + Земля"),
        (plant, fire, "Растение + Огонь"),
        (lightning, earth, "Молния + Земля"),
        (mud, fire, "Грязь + Огонь"),
        (plant, water, "Растение + Вода"),
    ]

    for elem1, elem2, desc in test_combinations:
        print(f"  {desc} = ", end="")
        result = elem1 + elem2
        print(f"{result if result else 'Нет результата'}")


def alchemy_guide():
    """Справочник по алхимии"""
    print("=" * 60)
    print("📚 СПРАВОЧНИК АЛХИМИКА")
    print("=" * 60)

    guide = """
    📖 БАЗОВЫЕ ЭЛЕМЕНТЫ:
      💧 Вода - основа жизни, текучесть, чистота
      💨 Воздух - свобода, движение, невесомость
      🔥 Огонь - энергия, разрушение, тепло
      🌍 Земля - стабильность, прочность, основа
      🌱 Жизнь - рост, развитие, органическое
      ⏳ Время - изменение, возраст, цикличность

    📖 СТАНДАРТНЫЕ РЕАКЦИИ:
      💧 Вода + 💨 Воздух = ⛈ Шторм
      💧 Вода + 🔥 Огонь = 💨 Пар
      💧 Вода + 🌍 Земля = 🟤 Грязь
      💨 Воздух + 🔥 Огонь = ⚡ Молния
      💨 Воздух + 🌍 Земля = 🌫 Пыль
      🔥 Огонь + 🌍 Земля = 🌋 Лава

    📖 СЕКРЕТНЫЕ РЕАКЦИИ:
      🌱 Жизнь + 💧 Вода = 🌿 Растение
      🌱 Жизнь + 🌍 Земля = 🐾 Животное
      🌱 Жизнь + 🔥 Огонь = ⚡ Энергия
      🌱 Жизнь + 💨 Воздух = 👻 Дух
      ⏳ Время + 🔥 Огонь = 🪵 Пепел
      ⏳ Время + 💧 Вода = ❄️ Лёд
      ⏳ Время + 🌍 Земля = 🦴 Ископаемое
      ⏳ Время + 💨 Воздух = 🌀 Пустота

    📖 ЭПИЧЕСКИЕ РЕАКЦИИ:
      🌿 Растение + 🔥 Огонь = 💨 Дым
      🐾 Животное + 💧 Вода = 🐟 Рыба
      ⚡ Энергия + 💨 Воздух = ⛈ Шторм
      👻 Дух + 🌍 Земля = 💎 Кристалл
      ❄️ Лёд + 🔥 Огонь = 💧 Вода
      💎 Кристалл + ⚡ Молния = 💎 Алмаз

    💡 СОВЕТ: Экспериментируйте! Не все комбинации дают результат,
    но именно в этом и заключается магия открытий!
    """

    print(guide)


def main():
    """Основная функция программы"""
    print("🔮 СИСТЕМА МАГИЧЕСКОЙ АЛХИМИИ")
    print("=" * 60)

    while True:
        print("\nВыберите действие:")
        print("1. 🧪 Использовать магический котел")
        print("2. 📊 Показать все комбинации")
        print("3. 📚 Открыть справочник алхимика")
        print("4. 🎮 Быстрая демонстрация")
        print("5. 🚪 Выход")

        choice = input("Ваш выбор (1-5): ").strip()

        if choice == "1":
            magic_cauldron()
        elif choice == "2":
            run_all_combinations()
        elif choice == "3":
            alchemy_guide()
        elif choice == "4":
            quick_demo()
        elif choice == "5":
            print("До новых открытий, алхимик! 🔮")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")


def quick_demo():
    """Быстрая демонстрация работы системы"""
    print("\n" + "=" * 60)
    print("🎮 БЫСТРАЯ ДЕМОНСТРАЦИЯ")
    print("=" * 60)

    # Создаем элементы
    water = Water()
    air = Air()
    fire = Fire()
    earth = Earth()
    life = Life()
    time = Time()

    # Демонстрация базовых комбинаций
    print("\n1. Базовые комбинации из условия:")
    combine_elements(water, air)  # Шторм
    combine_elements(water, fire)  # Пар
    combine_elements(water, earth)  # Грязь
    combine_elements(air, fire)  # Молния
    combine_elements(air, earth)  # Пыль
    combine_elements(fire, earth)  # Лава

    # Демонстрация собственных комбинаций
    print("\n2. Собственные комбинации:")
    combine_elements(life, water)  # Растение
    combine_elements(life, earth)  # Животное
    combine_elements(life, fire)  # Энергия
    combine_elements(life, air)  # Дух

    # Демонстрация цепочки преобразований
    print("\n3. Цепочка преобразований:")
    plant = combine_elements(life, water)  # Растение
    smoke = combine_elements(plant, fire) if plant else None  # Дым

    # Демонстрация None-результата
    print("\n4. Пример без результата:")
    combine_elements(water, water)  # None

    # Комбинация производных элементов
    print("\n5. Комбинация производных элементов:")
    storm = combine_elements(water, air)
    if storm:
        print(f"Создали: {storm}")
        print("Что будет, если Шторм смешать с Огнем?")
        combine_elements(storm, fire)


# Запуск тестов
if __name__ == "__main__":
    main()