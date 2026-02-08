class Child:
    """Класс ребенка"""

    def __init__(self, name, age, parent=None):
        """
        Инициализация ребенка

        Args:
            name (str): Имя ребенка
            age (int): Возраст ребенка
            parent (Parent): Родитель ребенка (опционально)
        """
        self.name = name
        self.age = age
        self.parent = parent

        # Состояния ребенка
        self.is_calm = True  # Спокоен ли (True - спокоен, False - плачет)
        self.is_hungry = False  # Голоден ли (False - сыт, True - голоден)

        # Уровни состояний для более детального контроля
        self.calm_level = 5  # Уровень спокойствия (0-10, где 10 - максимально спокоен)
        self.hunger_level = 2  # Уровень голода (0-10, где 10 - максимально голоден)

    def __str__(self):
        """Строковое представление ребенка"""
        calm_status = "спокоен" if self.is_calm else "плачет"
        hunger_status = "сыт" if not self.is_hungry else "голоден"

        return (f"👶 Ребёнок: {self.name}, {self.age} лет | "
                f"Состояние: {calm_status}, {hunger_status} | "
                f"Уровень спокойствия: {self.calm_level}/10, "
                f"Уровень голода: {self.hunger_level}/10")

    def update_states(self):
        """Обновляет булевые состояния на основе уровней"""
        # Если уровень спокойствия ниже 3, ребенок плачет
        self.is_calm = self.calm_level >= 3

        # Если уровень голода выше 6, ребенок голоден
        self.is_hungry = self.hunger_level >= 6

    def play(self):
        """Ребенок играет - теряет спокойствие и становится голоднее"""
        print(f"{self.name} играет...")
        self.calm_level = max(0, self.calm_level - 2)
        self.hunger_level = min(10, self.hunger_level + 1)
        self.update_states()

        if self.calm_level < 3:
            print(f"⚠️ {self.name} начинает плакать от усталости!")

    def time_passes(self):
        """Проходит время - ребенок становится голоднее и менее спокойным"""
        self.hunger_level = min(10, self.hunger_level + 1)
        self.calm_level = max(0, self.calm_level - 1)
        self.update_states()

        if self.hunger_level >= 6 and not self.is_hungry:
            print(f"⚠️ {self.name} проголодался!")
        if self.calm_level < 3 and self.is_calm:
            print(f"⚠️ {self.name} начал капризничать!")


class Parent:
    """Класс родителя"""

    def __init__(self, name, age):
        """
        Инициализация родителя

        Args:
            name (str): Имя родителя
            age (int): Возраст родителя
        """
        self.name = name
        self.age = age
        self.children = []  # Список детей

    def add_child(self, child_name, child_age):
        """
        Добавить ребенка

        Args:
            child_name (str): Имя ребенка
            child_age (int): Возраст ребенка

        Returns:
            Child or None: Объект ребенка или None если ошибка
        """
        # Проверка возраста (родитель должен быть старше минимум на 16 лет)
        if self.age - child_age < 16:
            print(
                f"❌ Ошибка: Родитель должен быть старше ребенка минимум на 16 лет!")
            print(f"   Родителю {self.age} лет, ребенку {child_age} лет")
            return None

        # Создаем ребенка и устанавливаем родителя
        child = Child(child_name, child_age, self)
        self.children.append(child)
        print(f"✅ Добавлен ребенок: {child_name}, {child_age} лет")
        return child

    def info(self):
        """Вывести информацию о родителе и детях"""
        print("\n" + "=" * 60)
        print(f"👨‍👩‍👧‍👦 ИНФОРМАЦИЯ О СЕМЬЕ")
        print("=" * 60)

        print(f"👤 Родитель: {self.name}, {self.age} лет")
        print(f"👶 Детей: {len(self.children)}")

        if self.children:
            print("\nДети:")
            for i, child in enumerate(self.children, 1):
                print(f"  {i}. {child}")

        # Статистика по детям
        calm_children = sum(1 for child in self.children if child.is_calm)
        hungry_children = sum(1 for child in self.children if child.is_hungry)

        print(f"\n📊 Статистика:")
        print(f"  Спокойных детей: {calm_children}/{len(self.children)}")
        print(
            f"  Сытых детей: {len(self.children) - hungry_children}/{len(self.children)}")

    def calm_child(self, child_index=None):
        """
        Успокоить ребенка

        Args:
            child_index (int, optional): Индекс ребенка в списке.
                                         Если None, успокаивает всех плачущих.

        Returns:
            bool: Успешно ли успокоили
        """
        if not self.children:
            print(f"{self.name} не имеет детей для успокоения.")
            return False

        if child_index is not None:
            # Успокоить конкретного ребенка
            if 0 <= child_index < len(self.children):
                child = self.children[child_index]
                if not child.is_calm:
                    print(f"🤗 {self.name} успокаивает {child.name}...")
                    child.calm_level = min(10, child.calm_level + 4)
                    child.update_states()
                    print(
                        f"✅ {child.name} теперь спокоен! (Уровень спокойствия: {child.calm_level}/10)")
                    return True
                else:
                    print(f"ℹ️ {child.name} уже спокоен.")
                    return False
            else:
                print(
                    f"❌ Некорректный индекс ребенка. Всего детей: {len(self.children)}")
                return False
        else:
            # Успокоить всех плачущих детей
            crying_children = [child for child in self.children if
                               not child.is_calm]

            if not crying_children:
                print("🎉 Все дети спокойны!")
                return True

            print(f"🤗 {self.name} успокаивает всех детей...")
            for child in crying_children:
                child.calm_level = min(10, child.calm_level + 4)
                child.update_states()
                print(f"  ✅ {child.name} успокоен")

            return True

    def feed_child(self, child_index=None):
        """
        Покормить ребенка

        Args:
            child_index (int, optional): Индекс ребенка в списке.
                                         Если None, кормит всех голодных.

        Returns:
            bool: Успешно ли покормили
        """
        if not self.children:
            print(f"{self.name} не имеет детей для кормления.")
            return False

        if child_index is not None:
            # Покормить конкретного ребенка
            if 0 <= child_index < len(self.children):
                child = self.children[child_index]
                if child.is_hungry:
                    print(f"🍎 {self.name} кормит {child.name}...")
                    child.hunger_level = max(0, child.hunger_level - 5)
                    child.update_states()
                    print(
                        f"✅ {child.name} теперь сыт! (Уровень голода: {child.hunger_level}/10)")
                    return True
                else:
                    print(f"ℹ️ {child.name} уже сыт.")
                    return False
            else:
                print(
                    f"❌ Некорректный индекс ребенка. Всего детей: {len(self.children)}")
                return False
        else:
            # Покормить всех голодных детей
            hungry_children = [child for child in self.children if
                               child.is_hungry]

            if not hungry_children:
                print("🎉 Все дети сыты!")
                return True

            print(f"🍎 {self.name} кормит всех детей...")
            for child in hungry_children:
                child.hunger_level = max(0, child.hunger_level - 5)
                child.update_states()
                print(f"  ✅ {child.name} накормлен")

            return True

    def check_children(self):
        """Проверить состояние всех детей и при необходимости помочь"""
        print(f"\n🔍 {self.name} проверяет детей...")

        need_calm = []
        need_feed = []

        for child in self.children:
            if not child.is_calm:
                need_calm.append(child)
            if child.is_hungry:
                need_feed.append(child)

        if not need_calm and not need_feed:
            print("✅ Все дети счастливы и здоровы!")
            return

        if need_calm:
            print(
                f"⚠️ Нужно успокоить: {', '.join(c.name for c in need_calm)}")
            self.calm_child()  # Успокаиваем всех

        if need_feed:
            print(
                f"⚠️ Нужно покормить: {', '.join(c.name for c in need_feed)}")
            self.feed_child()  # Кормим всех


def create_family():
    """Создание семьи с пользовательским вводом"""
    print("\n" + "=" * 60)
    print("👨‍👩‍👧‍👦 СОЗДАНИЕ СЕМЬИ")
    print("=" * 60)

    # Ввод данных родителя
    while True:
        parent_name = input("Введите имя родителя: ").strip()
        if parent_name:
            break
        print("❌ Имя не может быть пустым!")

    while True:
        try:
            parent_age = int(input("Введите возраст родителя: "))
            if parent_age >= 18:
                break
            print("❌ Родитель должен быть совершеннолетним (≥18 лет)!")
        except ValueError:
            print("❌ Введите целое число!")

    parent = Parent(parent_name, parent_age)

    # Добавление детей
    print(f"\nДобавим детей для {parent_name}:")

    while True:
        print("\n" + "-" * 40)
        print("1. Добавить ребенка")
        print("2. Завершить создание семьи")

        choice = input("Выберите действие (1-2): ").strip()

        if choice == "1":
            while True:
                child_name = input("Введите имя ребенка: ").strip()
                if child_name:
                    break
                print("❌ Имя не может быть пустым!")

            while True:
                try:
                    child_age = int(input("Введите возраст ребенка: "))
                    if child_age >= 0:
                        # Проверка возраста будет внутри add_child
                        break
                    print("❌ Возраст должен быть положительным!")
                except ValueError:
                    print("❌ Введите целое число!")

            child = parent.add_child(child_name, child_age)
            if child:
                print(f"✅ Ребенок {child_name} успешно добавлен в семью!")

        elif choice == "2":
            if not parent.children:
                print(
                    "⚠️ Вы не добавили ни одного ребенка. Хотите добавить? (да/нет)")
                if input().strip().lower() in ['да', 'yes', 'д', 'y']:
                    continue

            print(f"\n🎉 Семья создана!")
            print(f"   Родитель: {parent.name}, {parent.age} лет")
            print(f"   Детей: {len(parent.children)}")
            break

        else:
            print("❌ Пожалуйста, выберите 1 или 2.")

    return parent


def demo_family():
    """Создание демонстрационной семьи"""
    print("\n" + "=" * 60)
    print("👨‍👩‍👧‍👦 ДЕМОНСТРАЦИОННАЯ СЕМЬЯ")
    print("=" * 60)

    # Создаем родителя
    parent = Parent("Анна", 35)

    # Добавляем детей
    child1 = parent.add_child("Маша", 8)
    child2 = parent.add_child("Петя", 5)
    child3 = parent.add_child("Вова", 3)

    # Устанавливаем начальные состояния
    child1.calm_level = 7
    child1.hunger_level = 3
    child1.update_states()

    child2.calm_level = 2  # Плачет
    child2.hunger_level = 8  # Голоден
    child2.update_states()

    child3.calm_level = 4
    child3.hunger_level = 7  # Голоден
    child3.update_states()

    print("\n✅ Демонстрационная семья создана:")
    print(f"   Родитель: {parent.name}, {parent.age} лет")
    print(f"   Детей: {len(parent.children)}")

    return parent


def family_simulation(parent):
    """Симуляция жизни семьи"""
    print("\n" + "=" * 60)
    print("🏠 СИМУЛЯЦИЯ СЕМЕЙНОЙ ЖИЗНИ")
    print("=" * 60)

    day = 1
    max_days = 5  # Максимальное количество дней симуляции

    while day <= max_days:
        print(f"\n{'=' * 40}")
        print(f"📅 ДЕНЬ {day}")
        print(f"{'=' * 40}")

        # Утро
        print(f"\n🌅 Утро {parent.name} просыпается...")
        parent.info()

        # Проверяем детей
        parent.check_children()

        # Дети играют (теряют спокойствие и голодают)
        print(f"\n🎮 Дети играют...")
        for child in parent.children:
            child.play()

        # Обед
        print(f"\n🍽️ Обед:")
        parent.feed_child()

        # Вечер
        print(f"\n🌇 Вечер:")
        parent.check_children()

        # Время проходит
        print(f"\n⏰ Проходит время...")
        for child in parent.children:
            child.time_passes()

        # Проверяем, все ли дети в порядке
        unhappy_children = [c for c in parent.children if
                            not c.is_calm or c.is_hungry]

        if not unhappy_children:
            print(f"\n🎉 Все дети счастливы в конце дня {day}!")
        else:
            print(f"\n⚠️ В конце дня {day} есть недовольные дети:")
            for child in unhappy_children:
                print(f"  - {child.name}: ", end="")
                if not child.is_calm:
                    print("плачет", end="")
                if not child.is_calm and child.is_hungry:
                    print(" и ", end="")
                if child.is_hungry:
                    print("голоден", end="")
                print()

        # Показываем итоги дня
        parent.info()

        # Переход к следующему дню
        if day < max_days:
            print(f"\n⏭️ Переход к следующему дню...")

        day += 1

    print(f"\n{'=' * 60}")
    print("🏁 СИМУЛЯЦИЯ ЗАВЕРШЕНА!")
    print(f"{'=' * 60}")


def main():
    """Основная функция программы"""
    print("👨‍👩‍👧‍👦 СИМУЛЯТОР СЕМЬИ")
    print("=" * 60)

    while True:
        print("\nВыберите режим:")
        print("1. Создать свою семью")
        print("2. Использовать демонстрационную семью")
        print("3. Выход")

        choice = input("Ваш выбор (1-3): ").strip()

        if choice == "1":
            parent = create_family()
            if parent.children:
                parent.info()
                family_simulation(parent)
        elif choice == "2":
            parent = demo_family()
            parent.info()
            family_simulation(parent)
        elif choice == "3":
            print("👋 До свидания!")
            break
        else:
            print("❌ Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()