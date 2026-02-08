import random


class Warrior:
    """Класс для одного воина"""

    def __init__(self, name):
        self.name = name  # Имя воина
        self.health = 100  # Здоровье конкретного воина
        self.enemy = None  # Противник этого воина

    def attack(self):
        """Атаковать противника"""
        if self.enemy:
            self.enemy.health -= 20  # Противник теряет 20 HP
            print(f"{self.name} атаковал. "
                  f"У {self.enemy.name} осталось {self.enemy.health} очков здоровья.")

            # Проверяем, не умер ли противник
            if self.enemy.health <= 0:
                print(f"\n{self.name} одержал победу!")
                return True  # Бой окончен
        return False  # Бой продолжается


class Battle:
    """Класс для управления боем"""

    def __init__(self, warrior1_name="Воин_1", warrior2_name="Воин_2"):
        # Создаем двух воинов
        self.warrior1 = Warrior(warrior1_name)
        self.warrior2 = Warrior(warrior2_name)

        # Устанавливаем противников
        self.warrior1.enemy = self.warrior2
        self.warrior2.enemy = self.warrior1

        # Счетчик ходов (для информации)
        self.turn = 0

    def start_battle(self):
        """Начать бой"""
        print("=== НАЧАЛО БОЯ ===")
        print(f"{self.warrior1.name}: {self.warrior1.health} HP")
        print(f"{self.warrior2.name}: {self.warrior2.health} HP\n")

        # Бой продолжается, пока оба живы
        while self.warrior1.health > 0 and self.warrior2.health > 0:
            self.turn += 1
            print(f"--- Ход {self.turn} ---")

            # Случайный выбор атакующего
            if random.choice([True, False]):
                attacker = self.warrior1
            else:
                attacker = self.warrior2

            # Атака
            if attacker.attack():
                break  # Бой окончен

        print("\n=== БОЙ ЗАВЕРШЕН ===")


# Запуск программы
if __name__ == "__main__":
    battle = Battle()
    battle.start_battle()