import os
import sys
from enum import Enum


class Symbol(Enum):
    """Перечисление для символов на поле"""
    EMPTY = " "
    X = "❌"
    O = "⭕"


class Cell:
    """Класс клетки игрового поля"""

    def __init__(self, number):
        """
        Инициализация клетки

        Args:
            number (int): Номер клетки (1-9)
        """
        self.number = number
        self.symbol = Symbol.EMPTY
        self.is_occupied = False

    def set_symbol(self, symbol):
        """
        Установить символ в клетку

        Args:
            symbol (Symbol): Символ (X или O)

        Returns:
            bool: Успешно ли установлен символ
        """
        if not self.is_occupied and symbol != Symbol.EMPTY:
            self.symbol = symbol
            self.is_occupied = True
            return True
        return False

    def clear(self):
        """Очистить клетку"""
        self.symbol = Symbol.EMPTY
        self.is_occupied = False

    def __str__(self):
        """Строковое представление клетки"""
        return self.symbol.value


class Board:
    """Класс игрового поля"""

    WINNING_COMBINATIONS = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Горизонтали
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Вертикали
        [1, 5, 9], [3, 5, 7]  # Диагонали
    ]

    def __init__(self):
        """Инициализация поля с 9 клетками"""
        self.cells = [Cell(i) for i in range(1, 10)]
        self.moves_count = 0
        self.last_move = None

    def get_cell(self, number):
        """
        Получить клетку по номеру

        Args:
            number (int): Номер клетки (1-9)

        Returns:
            Cell or None: Объект клетки или None если не найден
        """
        if 1 <= number <= 9:
            return self.cells[number - 1]
        return None

    def change_cell_state(self, cell_number, symbol):
        """
        Изменить состояние клетки

        Args:
            cell_number (int): Номер клетки (1-9)
            symbol (Symbol): Символ для установки

        Returns:
            bool: Успешно ли изменено состояние
        """
        cell = self.get_cell(cell_number)
        if cell and not cell.is_occupied:
            success = cell.set_symbol(symbol)
            if success:
                self.moves_count += 1
                self.last_move = cell_number
                return True
        return False

    def check_win(self):
        """
        Проверить окончание игры (победу)

        Returns:
            Symbol or None: Символ победителя или None если нет победителя
        """
        for combo in self.WINNING_COMBINATIONS:
            cells = [self.get_cell(num) for num in combo]
            symbols = [cell.symbol for cell in cells]

            # Если все три клетки в комбинации заняты одним символом
            if (symbols[0] == symbols[1] == symbols[2] != Symbol.EMPTY):
                return symbols[0]
        return None

    def is_full(self):
        """
        Проверить, заполнено ли всё поле

        Returns:
            bool: True если поле полностью заполнено
        """
        return self.moves_count >= 9

    def is_game_over(self):
        """
        Проверить, окончена ли игра

        Returns:
            tuple: (bool, Symbol or None) - окончена ли игра и кто победил
        """
        winner = self.check_win()
        if winner:
            return True, winner
        if self.is_full():
            return True, None  # Ничья
        return False, None

    def get_available_moves(self):
        """
        Получить список доступных ходов

        Returns:
            list: Список номеров свободных клеток
        """
        return [cell.number for cell in self.cells if not cell.is_occupied]

    def clear(self):
        """Очистить игровое поле"""
        for cell in self.cells:
            cell.clear()
        self.moves_count = 0
        self.last_move = None

    def display(self, with_numbers=False):
        """
        Отобразить игровое поле

        Args:
            with_numbers (bool): Показывать ли номера клеток
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 40)
        print("🎮 КРЕСТИКИ-НОЛИКИ")
        print("=" * 40)

        print("\n   СХЕМА ПОЛЯ:" if with_numbers else "\n   ИГРОВОЕ ПОЛЕ:")
        print("   " + "-" * 13)

        for i in range(0, 9, 3):
            row_cells = self.cells[i:i + 3]
            row_numbers = [str(cell.number) for cell in row_cells]
            row_symbols = [str(cell) for cell in row_cells]

            if with_numbers:
                print(f"   | {' | '.join(row_numbers)} |")
            else:
                print(f"   | {' | '.join(row_symbols)} |")

            if i < 6:
                print("   |-----------|")

        print("   " + "-" * 13)

        # Показываем последний ход
        if self.last_move:
            cell = self.get_cell(self.last_move)
            print(
                f"\n   Последний ход: клетка {self.last_move} ({cell.symbol.value})")

        # Показываем доступные ходы
        available = self.get_available_moves()
        if available and not with_numbers:
            print(f"   Свободные клетки: {', '.join(map(str, available))}")


class Player:
    """Класс игрока"""

    def __init__(self, name, symbol):
        """
        Инициализация игрока

        Args:
            name (str): Имя игрока
            symbol (Symbol): Символ игрока (X или O)
        """
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.total_games = 0

    def make_move(self, board):
        """
        Сделать ход

        Args:
            board (Board): Игровое поле

        Returns:
            int or None: Номер выбранной клетки или None если ошибка
        """
        print(f"\n🎯 ХОД ИГРОКА: {self.name} ({self.symbol.value})")

        while True:
            try:
                # Показываем поле с номерами клеток
                board.display(with_numbers=True)

                move = input(
                    f"\n{self.name}, выберите номер клетки (1-9): ").strip()

                if move.lower() in ['выход', 'exit', 'quit', 'q']:
                    return None

                if not move.isdigit():
                    print("❌ Ошибка: введите число от 1 до 9!")
                    continue

                cell_number = int(move)

                if not 1 <= cell_number <= 9:
                    print("❌ Ошибка: номер клетки должен быть от 1 до 9!")
                    continue

                if cell_number not in board.get_available_moves():
                    print("❌ Ошибка: эта клетка уже занята!")
                    continue

                return cell_number

            except ValueError:
                print("❌ Ошибка: введите корректное число!")
            except KeyboardInterrupt:
                print("\n\n⚠️  Игра прервана пользователем.")
                return None

    def add_win(self):
        """Увеличить счетчик побед"""
        self.wins += 1
        self.total_games += 1

    def add_loss(self):
        """Увеличить счетчик игр (для статистики)"""
        self.total_games += 1

    def get_stats(self):
        """Получить статистику игрока"""
        if self.total_games == 0:
            win_rate = 0
        else:
            win_rate = (self.wins / self.total_games) * 100

        return {
            'name': self.name,
            'symbol': self.symbol.value,
            'wins': self.wins,
            'total_games': self.total_games,
            'win_rate': win_rate
        }

    def __str__(self):
        """Строковое представление игрока"""
        stats = self.get_stats()
        return (f"{self.name} ({self.symbol.value}) | "
                f"Победы: {stats['wins']} | "
                f"Всего игр: {stats['total_games']} | "
                f"Процент побед: {stats['win_rate']:.1f}%")


class Game:
    """Класс игры"""

    def __init__(self):
        """Инициализация игры"""
        self.board = Board()
        self.players = []
        self.current_player_index = 0
        self.game_state = "menu"  # menu, playing, finished
        self.round = 1

    def setup_players(self):
        """Настройка игроков"""
        print("\n" + "=" * 40)
        print("👥 НАСТРОЙКА ИГРОКОВ")
        print("=" * 40)

        # Выбор режима игры
        print("\nВыберите режим игры:")
        print("1. Играть против другого игрока")
        print("2. Играть против компьютера (простой уровень)")
        print("3. Играть против компьютера (средний уровень)")

        while True:
            mode = input("\nВаш выбор (1-3): ").strip()
            if mode in ['1', '2', '3']:
                break
            print("❌ Неверный выбор!")

        # Игрок 1 (всегда человек)
        print("\n" + "-" * 30)
        print("Игрок 1 (❌ Крестики):")
        name1 = input("Введите имя первого игрока: ").strip()
        if not name1:
            name1 = "Игрок 1"

        player1 = Player(name1, Symbol.X)
        self.players.append(player1)

        # Игрок 2
        print("\n" + "-" * 30)
        print("Игрок 2 (⭕ Нолики):")

        if mode == '1':
            name2 = input("Введите имя второго игрока: ").strip()
            if not name2:
                name2 = "Игрок 2"
            player2 = Player(name2, Symbol.O)
        else:
            name2 = "Компьютер"
            difficulty = "простой" if mode == '2' else "средний"
            player2 = AIPlayer(name2, Symbol.O, difficulty)

        self.players.append(player2)

        print(f"\n✅ Игроки созданы:")
        print(f"   {player1.name} играет за {player1.symbol.value}")
        print(f"   {player2.name} играет за {player2.symbol.value}")

    def run_single_turn(self, player):
        """
        Запуск одного хода игры

        Args:
            player (Player): Игрок, который делает ход

        Returns:
            bool: True если игра окончена, False если продолжается
        """
        # Для ИИ игрока
        if isinstance(player, AIPlayer):
            cell_number = player.make_move(self.board)
            if cell_number is None:
                return True  # Игра прервана
        else:
            # Для человека
            cell_number = player.make_move(self.board)
            if cell_number is None:
                return True  # Игра прервана

        # Изменяем состояние клетки
        success = self.board.change_cell_state(cell_number, player.symbol)
        if not success:
            print("❌ Не удалось сделать ход! Попробуйте снова.")
            return False

        # Проверяем окончание игры
        game_over, winner = self.board.is_game_over()

        if game_over:
            self.game_state = "finished"
            self.board.display()

            if winner:
                # Находим игрока-победителя
                winning_player = next(
                    (p for p in self.players if p.symbol == winner), None)
                if winning_player:
                    winning_player.add_win()
                    print(
                        f"\n🎉 ПОБЕДА! {winning_player.name} ({winning_player.symbol.value}) выиграл(а)!")

                    # Проигравший увеличивает счетчик игр
                    for p in self.players:
                        if p != winning_player:
                            p.add_loss()
            else:
                # Ничья
                print(f"\n🤝 НИЧЬЯ! Поле полностью заполнено.")
                for player in self.players:
                    player.add_loss()

            return True

        return False

    def run_single_game(self):
        """
        Запуск одной игры

        Returns:
            bool: True если игра завершена, False если прервана
        """
        self.board.clear()
        self.game_state = "playing"
        self.current_player_index = 0

        print(f"\n{'=' * 40}")
        print(f"🎮 ИГРА #{self.round}")
        print(f"{'=' * 40}")

        # Кто ходит первым
        print(
            f"\nПервым ходит: {self.players[0].name} ({self.players[0].symbol.value})")
        input("\nНажмите Enter чтобы начать...")

        while self.game_state == "playing":
            current_player = self.players[self.current_player_index]

            # Показываем текущее состояние поля
            self.board.display()

            # Выполняем ход
            game_ended = self.run_single_turn(current_player)

            if game_ended:
                if self.game_state == "finished":
                    return True
                else:
                    # Игра прервана
                    return False

            # Переключаем игрока
            self.current_player_index = (self.current_player_index + 1) % 2

        return True

    def show_statistics(self):
        """Показать статистику игроков"""
        print("\n" + "=" * 60)
        print("📊 СТАТИСТИКА ИГРОКОВ")
        print("=" * 60)

        for i, player in enumerate(self.players, 1):
            stats = player.get_stats()
            print(f"\n{i}. {player.name} ({player.symbol.value})")
            print(f"   Побед: {stats['wins']}")
            print(f"   Всего игр: {stats['total_games']}")
            print(f"   Процент побед: {stats['win_rate']:.1f}%")

        # Общая статистика
        total_games = sum(p.total_games for p in
                          self.players) // 2  # Каждая игра учитывается у обоих
        if total_games > 0:
            draws = total_games - sum(p.wins for p in self.players)
            print(f"\n📈 ОБЩАЯ СТАТИСТИКА:")
            print(f"   Всего сыграно игр: {total_games}")
            print(f"   Побед {self.players[0].name}: {self.players[0].wins}")
            print(f"   Побед {self.players[1].name}: {self.players[1].wins}")
            print(f"   Ничьих: {draws}")

    def run_games(self):
        """Основной метод запуска игр"""
        print("🎮 ДОБРО ПОЖАЛОВАТЬ В КРЕСТИКИ-НОЛИКИ!")

        # Настройка игроков
        self.setup_players()

        while True:
            # Запуск одной игры
            completed = self.run_single_game()

            if not completed:
                print("\n⚠️  Игра прервана.")
                break

            # Показываем статистику
            self.show_statistics()

            # Спрашиваем, хотят ли продолжить
            print("\n" + "=" * 40)
            print("🔄 ПРОДОЛЖИТЬ ИГРУ?")
            print("=" * 40)

            while True:
                choice = input(
                    "\nХотите сыграть еще раз? (да/нет): ").strip().lower()

                if choice in ['да', 'д', 'yes', 'y']:
                    self.round += 1

                    # Меняем символы местами для следующей игры
                    for player in self.players:
                        player.symbol = Symbol.O if player.symbol == Symbol.X else Symbol.X

                    # Первый ход делает другой игрок
                    self.players.reverse()

                    print(
                        f"\nТеперь {self.players[0].name} играет за {self.players[0].symbol.value}")
                    print(f"и ходит первым!")
                    input("\nНажмите Enter чтобы продолжить...")
                    break

                elif choice in ['нет', 'н', 'no', 'n']:
                    print("\n" + "=" * 60)
                    print("🎮 ФИНАЛЬНАЯ СТАТИСТИКА")
                    print("=" * 60)
                    self.show_statistics()
                    print("\n👋 Спасибо за игру! До встречи!")
                    return
                else:
                    print("❌ Пожалуйста, ответьте 'да' или 'нет'.")

    def show_rules(self):
        """Показать правила игры"""
        print("\n" + "=" * 60)
        print("📖 ПРАВИЛА ИГРЫ КРЕСТИКИ-НОЛИКИ")
        print("=" * 60)

        rules = """
        ПРАВИЛА:
        1. Игроки по очереди ставят свои символы на поле 3x3.
        2. Игрок 1 ставит ❌ (крестики), игрок 2 ставит ⭕ (нолики).
        3. Цель игры — первым выстроить в ряд 3 своих символа:
           • По горизонтали (ряды: 1-2-3, 4-5-6, 7-8-9)
           • По вертикали (колонки: 1-4-7, 2-5-8, 3-6-9)
           • По диагонали (1-5-9 или 3-5-7)
        4. Если все клетки заполнены, но ни один игрок не выиграл — ничья.

        УПРАВЛЕНИЕ:
        • Для выбора клетки введите её номер (от 1 до 9)
        • Нумерация клеток:
             1 | 2 | 3
            -----------
             4 | 5 | 6
            -----------
             7 | 8 | 9

        ПОДСКАЗКИ:
        • Всегда показываются доступные для хода клетки
        • Для выхода из игры введите 'выход'
        """

        print(rules)
        input("\nНажмите Enter чтобы вернуться в меню...")


class AIPlayer(Player):
    """Класс ИИ-игрока"""

    def __init__(self, name, symbol, difficulty="простой"):
        """
        Инициализация ИИ-игрока

        Args:
            name (str): Имя ИИ
            symbol (Symbol): Символ ИИ
            difficulty (str): Уровень сложности (простой/средний)
        """
        super().__init__(name, symbol)
        self.difficulty = difficulty

    def make_move(self, board):
        """
        Сделать ход (ИИ)

        Args:
            board (Board): Игровое поле

        Returns:
            int: Номер выбранной клетки
        """
        print(f"\n🤖 Ход компьютера ({self.name})...")

        available_moves = board.get_available_moves()

        if not available_moves:
            return None

        if self.difficulty == "простой":
            # Простой ИИ: случайный ход
            import random
            return random.choice(available_moves)

        elif self.difficulty == "средний":
            # Средний ИИ: пытается выиграть или блокировать противника
            import random

            # 1. Проверить, может ли ИИ выиграть следующим ходом
            for move in available_moves:
                # Создаем копию доски для проверки
                test_board = self._simulate_move(board, move, self.symbol)
                if test_board.check_win() == self.symbol:
                    print(f"   Компьютер нашел выигрышный ход: клетка {move}")
                    return move

            # 2. Проверить, может ли противник выиграть следующим ходом
            opponent_symbol = Symbol.O if self.symbol == Symbol.X else Symbol.X
            for move in available_moves:
                test_board = self._simulate_move(board, move, opponent_symbol)
                if test_board.check_win() == opponent_symbol:
                    print(f"   Компьютер блокирует противника: клетка {move}")
                    return move

            # 3. Если центр свободен, занять его
            if 5 in available_moves:
                print(f"   Компьютер занимает центр: клетка 5")
                return 5

            # 4. Если углы свободны, занять случайный угол
            corners = [1, 3, 7, 9]
            available_corners = [c for c in corners if c in available_moves]
            if available_corners:
                move = random.choice(available_corners)
                print(f"   Компьютер занимает угол: клетка {move}")
                return move

            # 5. Случайный ход
            move = random.choice(available_moves)
            print(f"   Компьютер делает случайный ход: клетка {move}")
            return move

        # На всякий случай: если не выбран уровень сложности
        import random
        return random.choice(available_moves)

    def _simulate_move(self, board, cell_number, symbol):
        """
        Симулировать ход на копии доски

        Args:
            board (Board): Исходное поле
            cell_number (int): Номер клетки
            symbol (Symbol): Символ для установки

        Returns:
            Board: Копия доски с выполненным ходом
        """
        # Создаем новую доску и копируем состояние
        new_board = Board()
        for i in range(1, 10):
            cell = board.get_cell(i)
            if cell.is_occupied:
                new_board.change_cell_state(i, cell.symbol)

        # Выполняем ход
        new_board.change_cell_state(cell_number, symbol)
        return new_board


def main():
    """Основная функция программы"""
    game = Game()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("🎮 ГЛАВНОЕ МЕНЮ - КРЕСТИКИ-НОЛИКИ")
        print("=" * 60)

        print("\nВыберите действие:")
        print("1. 🎮 Начать новую игру")
        print("2. 📖 Показать правила")
        print("3. 📊 Показать статистику (если была игра)")
        print("4. 🚪 Выход")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == "1":
            game = Game()  # Новая игра
            game.run_games()
        elif choice == "2":
            game.show_rules()
        elif choice == "3":
            if game.players:
                game.show_statistics()
                input("\nНажмите Enter чтобы продолжить...")
            else:
                print(
                    "\n❌ Статистика недоступна. Сначала сыграйте хотя бы одну игру!")
                input("\nНажмите Enter чтобы продолжить...")
        elif choice == "4":
            print("\n👋 До свидания! Спасибо за игру!")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, выберите 1-4.")
            input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()