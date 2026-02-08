import random
from datetime import datetime, timedelta


class House:
    """Класс дома с ресурсами"""

    def __init__(self, food=50, money=0):
        """
        Инициализация дома

        Args:
            food (int): Начальное количество еды (по умолчанию 50)
            money (int): Начальное количество денег (по умолчанию 0)
        """
        self.food = food
        self.money = money
        self.residents = []  # Список жильцов

    def __str__(self):
        """Строковое представление дома"""
        return (f"🏠 Дом | Еда: {self.food} | Деньги: {self.money}₽ | "
                f"Жильцов: {len(self.residents)}")

    def add_resident(self, person):
        """Добавить жильца в дом"""
        self.residents.append(person)
        person.house = self

    def get_status(self):
        """Получить статус дома"""
        return {
            'food': self.food,
            'money': self.money,
            'residents': len(self.residents),
            'resident_names': [p.name for p in self.residents]
        }


class Person:
    """Класс человека"""

    def __init__(self, name, house=None):
        """
        Инициализация человека

        Args:
            name (str): Имя человека
            house (House, optional): Дом, в котором живет человек
        """
        self.name = name
        self.satiety = 50  # Сытость (0-100)
        self.house = house
        self.is_alive = True
        self.days_alive = 0
        self.stats = {
            'ate_times': 0,
            'worked_times': 0,
            'played_times': 0,
            'shopped_times': 0,
            'earned_money': 0,
            'spent_money': 0,
            'consumed_food': 0,
            'bought_food': 0
        }

        if house:
            house.add_resident(self)

    def __str__(self):
        """Строковое представление человека"""
        status = "😊 Жив" if self.is_alive else "💀 Мёртв"
        return (f"👤 {self.name} | Сытость: {self.satiety}/100 | "
                f"Дней прожито: {self.days_alive} | {status}")

    def eat(self):
        """Поесть (+30 сытости, -10 еды из дома)"""
        if self.house.food >= 10:
            self.satiety = min(100, self.satiety + 30)
            self.house.food -= 10
            self.stats['ate_times'] += 1
            self.stats['consumed_food'] += 10
            print(
                f"  🍽️  {self.name} поел. Сытость: {self.satiety}, Еды в доме: {self.house.food}")
            return True
        else:
            print(f"  ⚠️  {self.name} хотел поесть, но в доме нет еды!")
            return False

    def work(self):
        """Поработать (-20 сытости, +50 денег)"""
        if self.satiety >= 20:
            self.satiety -= 20
            self.house.money += 50
            self.stats['worked_times'] += 1
            self.stats['earned_money'] += 50
            print(
                f"  💼 {self.name} поработал. Сытость: {self.satiety}, Денег в доме: {self.house.money}₽")
            return True
        else:
            print(f"  ⚠️  {self.name} слишком голоден для работы!")
            return False

    def play(self):
        """Поиграть (-10 сытости)"""
        if self.satiety >= 10:
            self.satiety -= 10
            self.stats['played_times'] += 1
            print(f"  🎮 {self.name} поиграл. Сытость: {self.satiety}")
            return True
        else:
            print(f"  ⚠️  {self.name} слишком голоден для игр!")
            return False

    def shop(self):
        """Сходить в магазин (+30 еды, -30 денег)"""
        if self.house.money >= 30:
            self.house.food += 30
            self.house.money -= 30
            self.stats['shopped_times'] += 1
            self.stats['spent_money'] += 30
            self.stats['bought_food'] += 30
            print(
                f"  🛒 {self.name} сходил в магазин. Еды: {self.house.food}, Денег: {self.house.money}₽")
            return True
        else:
            print(f"  ⚠️  {self.name} хотел купить еды, но нет денег!")
            return False

    def live_one_day(self, day_number):
        """Прожить один день"""
        if not self.is_alive:
            return False

        print(f"\n📅 День {day_number}: {self.name}")
        print(
            f"  Начальное состояние: сытость={self.satiety}, еда в доме={self.house.food}, деньги={self.house.money}₽")

        # Генерируем случайное число от 1 до 6
        dice_roll = random.randint(1, 6)
        print(f"  🎲 Выпало на кубике: {dice_roll}")

        # Логика выбора действия
        action_taken = False

        # 1. Если сытость < 20, нужно поесть
        if self.satiety < 20:
            print(f"  🚨 Срочно нужно поесть! Сытость: {self.satiety}")
            action_taken = self.eat()

        # 2. Иначе, если еды в доме < 10, сходить в магазин
        elif not action_taken and self.house.food < 10:
            print(f"  🛒 Мало еды в доме: {self.house.food}")
            action_taken = self.shop()

        # 3. Иначе, если денег в доме < 50, работать
        elif not action_taken and self.house.money < 50:
            print(f"  💰 Мало денег в доме: {self.house.money}₽")
            action_taken = self.work()

        # 4. Иначе, если кубик == 1, работать
        elif not action_taken and dice_roll == 1:
            print(f"  🎲 Выпала 1 - поработать")
            action_taken = self.work()

        # 5. Иначе, если кубик == 2, поесть
        elif not action_taken and dice_roll == 2:
            print(f"  🎲 Выпала 2 - поесть")
            action_taken = self.eat()

        # 6. Иначе играть
        elif not action_taken:
            print(f"  🎲 Выпало {dice_roll} - поиграть")
            action_taken = self.play()

        # Если действие не удалось выполнить (например, нет еды или денег)
        if not action_taken:
            print(
                f"  ⚠️  {self.name} не смог выполнить запланированное действие!")

        # Проверяем, не умер ли человек
        if self.satiety <= 0:
            self.is_alive = False
            print(f"  💀 {self.name} умер от голода!")
            return False

        # Увеличиваем счетчик прожитых дней
        if self.is_alive:
            self.days_alive += 1
            # Естественное снижение сытости (на 5 единиц в день)
            self.satiety = max(0, self.satiety - 5)
            if self.satiety <= 0:
                self.is_alive = False
                print(f"  💀 {self.name} умер от голода в конце дня!")
                return False

        return self.is_alive

    def get_stats(self):
        """Получить статистику человека"""
        return {
            'name': self.name,
            'days_alive': self.days_alive,
            'is_alive': self.is_alive,
            'final_satiety': self.satiety,
            'stats': self.stats
        }


class Simulation:
    """Класс для управления симуляцией"""

    def __init__(self, days_to_simulate=365):
        """
        Инициализация симуляции

        Args:
            days_to_simulate (int): Количество дней для симуляции
        """
        self.days = days_to_simulate
        self.houses = []
        self.people = []
        self.start_date = None
        self.end_date = None
        self.simulation_results = []

    def create_scenario(self, scenario_number=1):
        """Создать сценарий симуляции"""
        print(f"\n{'=' * 60}")
        print(f"🏘️  СЦЕНАРИЙ {scenario_number}")
        print(f"{'=' * 60}")

        if scenario_number == 1:
            # Сценарий 1: Двое в одном доме
            house1 = House(food=50, money=0)
            person1 = Person("Артём", house1)
            person2 = Person("Мария", house1)

            self.houses = [house1]
            self.people = [person1, person2]

            print("Создана ситуация: 2 человека в одном доме")
            print(f"Дом 1: {house1}")

        elif scenario_number == 2:
            # Сценарий 2: Каждый в своем доме
            house1 = House(food=50, money=0)
            house2 = House(food=30, money=20)

            person1 = Person("Иван", house1)
            person2 = Person("Ольга", house2)

            self.houses = [house1, house2]
            self.people = [person1, person2]

            print("Создана ситуация: 2 человека в разных домах")
            print(f"Дом 1: {house1}")
            print(f"Дом 2: {house2}")

        elif scenario_number == 3:
            # Сценарий 3: Трое в одном доме
            house1 = House(food=60, money=10)

            person1 = Person("Алексей", house1)
            person2 = Person("Екатерина", house1)
            person3 = Person("Дмитрий", house1)

            self.houses = [house1]
            self.people = [person1, person2, person3]

            print("Создана ситуация: 3 человека в одном доме")
            print(f"Дом 1: {house1}")

        else:
            # Пользовательский сценарий
            print("Создание пользовательского сценария...")
            num_houses = int(input("Сколько домов создать? "))
            num_people = int(input("Сколько людей создать? "))

            self.houses = []
            self.people = []

            for i in range(num_houses):
                food = int(
                    input(f"Еда в доме {i + 1} (по умолчанию 50): ") or "50")
                money = int(
                    input(f"Деньги в доме {i + 1} (по умолчанию 0): ") or "0")
                house = House(food=food, money=money)
                self.houses.append(house)

            for i in range(num_people):
                name = input(f"Имя человека {i + 1}: ")
                house_index = int(input(
                    f"В каком доме будет жить {name} (1-{num_houses})? ")) - 1

                if 0 <= house_index < len(self.houses):
                    person = Person(name, self.houses[house_index])
                    self.people.append(person)
                else:
                    print("Неверный индекс дома, создаю отдельный дом...")
                    house = House()
                    person = Person(name, house)
                    self.houses.append(house)
                    self.people.append(person)

        print(
            f"\nВсего создано: {len(self.houses)} домов, {len(self.people)} человек")

    def run_simulation(self):
        """Запустить симуляцию"""
        print(f"\n{'=' * 60}")
        print(f"🚀 ЗАПУСК СИМУЛЯЦИИ НА {self.days} ДНЕЙ")
        print(f"{'=' * 60}")

        self.start_date = datetime.now()

        # Проживаем каждый день
        for day in range(1, self.days + 1):
            print(f"\n{'=' * 40}")
            print(f"📅 ДЕНЬ {day} ИЗ {self.days}")
            print(f"{'=' * 40}")

            # Каждый человек проживает день
            all_alive = True
            for person in self.people:
                if person.is_alive:
                    person.live_one_day(day)
                    if not person.is_alive:
                        all_alive = False
                else:
                    print(f"\n📅 День {day}: {person.name} уже мертв")

            # Если все умерли, прекращаем симуляцию
            if not any(p.is_alive for p in self.people):
                print(
                    f"\n💀 Все жители умерли! Симуляция завершена досрочно на день {day}")
                break

            # Показываем сводку по домам
            print(f"\n📊 СВОДКА ПО ДОМАМ:")
            for i, house in enumerate(self.houses, 1):
                print(f"  Дом {i}: {house}")

        self.end_date = datetime.now()
        self._collect_results()

    def _collect_results(self):
        """Собрать результаты симуляции"""
        for person in self.people:
            self.simulation_results.append(person.get_stats())

    def show_results(self):
        """Показать результаты симуляции"""
        print(f"\n{'=' * 80}")
        print("📊 РЕЗУЛЬТАТЫ СИМУЛЯЦИИ")
        print(f"{'=' * 80}")

        duration = self.end_date - self.start_date if self.end_date and self.start_date else timedelta(
            0)
        print(f"Длительность симуляции: {duration.total_seconds():.2f} секунд")
        print(f"Смоделировано дней: {self.days}")
        print(f"Всего людей: {len(self.people)}")

        alive_count = sum(
            1 for result in self.simulation_results if result['is_alive'])
        dead_count = len(self.people) - alive_count

        print(f"\n🏆 ВЫЖИВШИЕ: {alive_count} человек")
        print(f"💀 ПОГИБШИЕ: {dead_count} человек")

        # Статистика по каждому человеку
        print(f"\n{'=' * 80}")
        print("👤 ПОДРОБНАЯ СТАТИСТИКА ПО КАЖДОМУ ЧЕЛОВЕКУ:")
        print(f"{'=' * 80}")

        for result in self.simulation_results:
            status = "✅ ЖИВ" if result['is_alive'] else "💀 МЕРТВ"
            print(f"\n{result['name']} - {status}")
            print(f"  Прожито дней: {result['days_alive']}")
            print(f"  Финальная сытость: {result['final_satiety']}")

            stats = result['stats']
            print(f"  Статистика действий:")
            print(
                f"    • Поел раз: {stats['ate_times']} (съел {stats['consumed_food']} еды)")
            print(
                f"    • Поработал раз: {stats['worked_times']} (заработал {stats['earned_money']}₽)")
            print(f"    • Поиграл раз: {stats['played_times']}")
            print(
                f"    • Сходил в магазин раз: {stats['shopped_times']} (купил {stats['bought_food']} еды за {stats['spent_money']}₽)")

        # Статистика по домам
        print(f"\n{'=' * 80}")
        print("🏠 СОСТОЯНИЕ ДОМОВ ПОСЛЕ СИМУЛЯЦИИ:")
        print(f"{'=' * 80}")

        for i, house in enumerate(self.houses, 1):
            status = house.get_status()
            print(f"\nДом {i}:")
            print(f"  Еды осталось: {status['food']}")
            print(f"  Денег осталось: {status['money']}₽")
            print(f"  Жильцы: {', '.join(status['resident_names'])}")

        # Анализ выживаемости
        print(f"\n{'=' * 80}")
        print("📈 АНАЛИЗ ВЫЖИВАЕМОСТИ:")
        print(f"{'=' * 80}")

        if alive_count > 0:
            survival_rate = (alive_count / len(self.people)) * 100
            print(f"Процент выживания: {survival_rate:.1f}%")

            # Находим лучшего выжившего
            survivors = [r for r in self.simulation_results if r['is_alive']]
            if survivors:
                best_survivor = max(survivors, key=lambda x: x['days_alive'])
                print(
                    f"Лучший выживший: {best_survivor['name']} (прожил {best_survivor['days_alive']} дней)")

        # Рекомендации
        print(f"\n{'=' * 80}")
        print("💡 РЕКОМЕНДАЦИИ ДЛЯ СОВМЕСТНОГО ПРОЖИВАНИЯ:")
        print(f"{'=' * 80}")

        if alive_count == len(self.people):
            print("✅ Отличный результат! Все выжили!")
            print("Рекомендация: Можете смело жить вместе!")
        elif alive_count >= len(self.people) * 0.5:
            print("⚠️  Умеренных успех. Не все выжили.")
            print("Рекомендация: Нужно лучше планировать ресурсы.")
        else:
            print("❌ Плохой результат. Большинство не выжило.")
            print(
                "Рекомендация: Лучше жить отдельно или улучшить планирование.")

    def run_multiple_tests(self, num_tests=5):
        """Запустить несколько тестов для статистики"""
        print(f"\n{'=' * 80}")
        print(f"📊 ЗАПУСК {num_tests} ТЕСТОВЫХ СИМУЛЯЦИЙ")
        print(f"{'=' * 80}")

        test_results = []

        for test_num in range(1, num_tests + 1):
            print(f"\n🧪 ТЕСТ {test_num} ИЗ {num_tests}")

            # Создаем новый сценарий для каждого теста
            house = House(food=50, money=0)
            person1 = Person("Артём", house)
            person2 = Person("Мария", house)

            # Запускаем симуляцию
            all_alive = True
            for day in range(1, self.days + 1):
                for person in [person1, person2]:
                    if person.is_alive:
                        if not person.live_one_day(day):
                            all_alive = False

                if not any([person1.is_alive, person2.is_alive]):
                    break

            # Собираем результаты теста
            survived = person1.is_alive and person2.is_alive
            test_results.append({
                'test_num': test_num,
                'survived': survived,
                'person1_days': person1.days_alive,
                'person2_days': person2.days_alive,
                'final_food': house.food,
                'final_money': house.money
            })

            status = "✅ ОБА ВЫЖИЛИ" if survived else "💀 КТО-ТО УМЕР"
            print(f"  Результат: {status}")

        # Анализ тестов
        print(f"\n{'=' * 80}")
        print("📈 СТАТИСТИКА ПО ВСЕМ ТЕСТАМ:")
        print(f"{'=' * 80}")

        successful_tests = sum(1 for r in test_results if r['survived'])
        success_rate = (successful_tests / num_tests) * 100

        print(f"Всего тестов: {num_tests}")
        print(f"Успешных тестов (оба выжили): {successful_tests}")
        print(f"Процент успеха: {success_rate:.1f}%")

        if success_rate >= 80:
            print(
                "\n🎉 Отличные шансы! С высокой вероятностью сможете жить вместе.")
        elif success_rate >= 50:
            print("\n⚠️  Шансы средние. Есть риск, но можно попробовать.")
        else:
            print("\n❌ Низкие шансы. Рискованно жить вместе.")


def main():
    """Основная функция программы"""
    print("🏘️  СИМУЛЯТОР СОВМЕСТНОГО ПРОЖИВАНИЯ")
    print("=" * 60)
    print("Определите, стоит ли жить вместе или лучше в одиночестве!")

    while True:
        print("\n" + "=" * 60)
        print("ГЛАВНОЕ МЕНЮ:")
        print("1. 🎮 Запустить симуляцию с выбором сценария")
        print("2. 📊 Запустить несколько тестов для статистики")
        print("3. ℹ️  Показать описание логики симуляции")
        print("4. 🚪 Выход")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == "1":
            # Выбор сценария
            print("\n" + "=" * 60)
            print("ВЫБЕРИТЕ СЦЕНАРИЙ:")
            print("1. Двое в одном доме (Артём и Мария)")
            print("2. Каждый в своем доме")
            print("3. Трое в одном доме")
            print("4. Создать пользовательский сценарий")

            scenario_choice = input("\nВыберите сценарий (1-4): ").strip()

            # Создаем симуляцию
            sim = Simulation(days_to_simulate=365)

            if scenario_choice in ["1", "2", "3"]:
                sim.create_scenario(int(scenario_choice))
            elif scenario_choice == "4":
                sim.create_scenario(4)
            else:
                print("Неверный выбор, использую сценарий 1")
                sim.create_scenario(1)

            # Запускаем симуляцию
            sim.run_simulation()
            sim.show_results()

            input("\nНажмите Enter для продолжения...")

        elif choice == "2":
            # Множественные тесты
            print("\n" + "=" * 60)
            print("МНОЖЕСТВЕННЫЕ ТЕСТЫ")

            try:
                num_tests = int(input(
                    "Сколько тестов запустить? (рекомендуется 5-10): ") or "5")
                sim = Simulation(days_to_simulate=365)
                sim.run_multiple_tests(num_tests)
            except ValueError:
                print("❌ Неверное число!")

            input("\nНажмите Enter для продолжения...")

        elif choice == "3":
            # Описание логики
            print("\n" + "=" * 80)
            print("📖 ОПИСАНИЕ ЛОГИКИ СИМУЛЯЦИИ")
            print("=" * 80)

            description = """
            КАЖДЫЙ ДЕНЬ ЧЕЛОВЕК ВЫПОЛНЯЕТ ОДНО ДЕЙСТВИЕ ПО ПРИОРИТЕТУ:

            1. 🚨 Если сытость < 20 → ПОЕСТЬ (+30 сытости, -10 еды)
            2. 🛒 Если еды в доме < 10 → В МАГАЗИН (+30 еды, -30 денег)
            3. 💰 Если денег в доме < 50 → РАБОТАТЬ (-20 сытости, +50 денег)
            4. 🎲 Если выпало 1 на кубике → РАБОТАТЬ
            5. 🎲 Если выпало 2 на кубике → ПОЕСТЬ
            6. 🎮 В остальных случаях → ИГРАТЬ (-10 сытости)

            ДОПОЛНИТЕЛЬНО:
            • Каждый день сытость уменьшается на 5 единиц
            • Если сытость ≤ 0 → человек умирает
            • В начале: сытость=50, еда=50, деньги=0

            ЦЕЛЬ: Прожить 365 дней, не умерев от голода!
            """

            print(description)
            input("\nНажмите Enter для продолжения...")

        elif choice == "4":
            print("\nСпасибо за использование симулятора! До свидания! 👋")
            break

        else:
            print("❌ Неверный выбор! Пожалуйста, выберите 1-4.")


if __name__ == "__main__":
    main()