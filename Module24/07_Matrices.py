import copy
import math
import random


class Matrix:
    """Класс для работы с матрицами с поддержкой основных операций линейной алгебры"""

    def __init__(self, rows, cols=None, data=None, fill_value=0):
        """
        Инициализация матрицы

        Args:
            rows (int): Количество строк
            cols (int, optional): Количество столбцов (если None, то cols=rows)
            data (list of list, optional): Данные матрицы
            fill_value (int/float, optional): Значение для заполнения при создании матрицы
        """
        if cols is None:
            cols = rows  # Создание квадратной матрицы

        self.rows = rows
        self.cols = cols

        if data is not None:
            # Проверяем, что данные корректны
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError(
                    f"Данные не соответствуют размеру {rows}x{cols}")
            self.data = [list(row) for row in data]
        else:
            # Создаем матрицу, заполненную fill_value
            self.data = [[fill_value for _ in range(cols)] for _ in
                         range(rows)]

    def __str__(self):
        """Строковое представление матрицы"""
        # Определяем максимальную длину элемента для форматирования
        max_len = 0
        for row in self.data:
            for element in row:
                element_str = f"{element:.6f}" if isinstance(element,
                                                             float) else str(
                    element)
                max_len = max(max_len, len(element_str))

        result = []
        for row in self.data:
            row_str = []
            for element in row:
                # Форматируем числа: целые показываем как целые, вещественные с 6 знаками
                if isinstance(element, float):
                    element_str = f"{element:>{max_len}.6f}"
                else:
                    element_str = f"{element:>{max_len}}"
                row_str.append(element_str)
            result.append("  ".join(row_str))

        return "\n".join(result)

    def __repr__(self):
        """Представление для отладки"""
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """Проверка на равенство матриц"""
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """Перегрузка оператора +"""
        return self.add(other)

    def __sub__(self, other):
        """Перегрузка оператора -"""
        return self.subtract(other)

    def __mul__(self, other):
        """
        Перегрузка оператора *
        Поддерживает умножение на другую матрицу или на скаляр
        """
        if isinstance(other, (int, float)):
            return self.scalar_multiply(other)
        elif isinstance(other, Matrix):
            return self.multiply(other)
        else:
            raise TypeError("Неподдерживаемый тип для умножения")

    def __getitem__(self, index):
        """Получение элемента или строки по индексу"""
        if isinstance(index, tuple):
            i, j = index
            return self.data[i][j]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        """Установка элемента или строки по индексу"""
        if isinstance(index, tuple):
            i, j = index
            self.data[i][j] = value
        else:
            if isinstance(value, list) and len(value) == self.cols:
                self.data[index] = value
            else:
                raise ValueError(
                    f"Строка должна содержать {self.cols} элементов")

    def add(self, other):
        """
        Сложение матриц

        Args:
            other (Matrix): Матрица для сложения

        Returns:
            Matrix: Результат сложения

        Raises:
            ValueError: Если размеры матриц не совпадают
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Нельзя сложить матрицы размеров {self.rows}x{self.cols} и {other.rows}x{other.cols}")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def subtract(self, other):
        """
        Вычитание матриц

        Args:
            other (Matrix): Матрица для вычитания

        Returns:
            Matrix: Результат вычитания

        Raises:
            ValueError: Если размеры матриц не совпадают
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Нельзя вычесть матрицы размеров {self.rows}x{self.cols} и {other.rows}x{other.cols}")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]

        return result

    def multiply(self, other):
        """
        Умножение матриц

        Args:
            other (Matrix): Матрица для умножения

        Returns:
            Matrix: Результат умножения

        Raises:
            ValueError: Если число столбцов первой матрицы не равно числу строк второй
        """
        if self.cols != other.rows:
            raise ValueError(
                f"Нельзя умножить матрицы: {self.cols} != {other.rows}")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum_val

        return result

    def scalar_multiply(self, scalar):
        """
        Умножение матрицы на скаляр

        Args:
            scalar (int/float): Скаляр для умножения

        Returns:
            Matrix: Результат умножения
        """
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar

        return result

    def transpose(self):
        """
        Транспонирование матрицы

        Returns:
            Matrix: Транспонированная матрица
        """
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]

        return result

    def determinant(self):
        """
        Вычисление определителя матрицы (только для квадратных матриц)

        Returns:
            float: Определитель матрицы

        Raises:
            ValueError: Если матрица не квадратная
        """
        if self.rows != self.cols:
            raise ValueError(
                "Определитель можно вычислить только для квадратной матрицы")

        # Для матрицы 1x1
        if self.rows == 1:
            return self.data[0][0]

        # Для матрицы 2x2
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * \
                self.data[1][0]

        # Для матрицы 3x3 (правило Сарруса)
        if self.rows == 3:
            a = self.data
            return (a[0][0] * a[1][1] * a[2][2] +
                    a[0][1] * a[1][2] * a[2][0] +
                    a[0][2] * a[1][0] * a[2][1] -
                    a[0][2] * a[1][1] * a[2][0] -
                    a[0][1] * a[1][0] * a[2][2] -
                    a[0][0] * a[1][2] * a[2][1])

        # Общий случай (разложение по первой строке)
        det = 0
        for j in range(self.cols):
            # Создаем минор, исключая первую строку и j-й столбец
            minor = Matrix(self.rows - 1, self.cols - 1)
            for i in range(1, self.rows):
                col_idx = 0
                for k in range(self.cols):
                    if k != j:
                        minor.data[i - 1][col_idx] = self.data[i][k]
                        col_idx += 1

            # Рекурсивно вычисляем определитель минора
            sign = 1 if j % 2 == 0 else -1
            det += sign * self.data[0][j] * minor.determinant()

        return det

    def inverse(self):
        """
        Вычисление обратной матрицы (только для квадратных матриц с ненулевым определителем)

        Returns:
            Matrix: Обратная матрица

        Raises:
            ValueError: Если матрица не квадратная или определитель равен 0
        """
        if self.rows != self.cols:
            raise ValueError(
                "Обратную матрицу можно вычислить только для квадратной матрицы")

        det = self.determinant()
        if abs(det) < 1e-10:  # Маленький порог для нуля
            raise ValueError(
                "Матрица вырожденная, обратной матрицы не существует")

        # Для матрицы 2x2
        if self.rows == 2:
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]

            result = Matrix(2, 2)
            result.data = [[d / det, -b / det], [-c / det, a / det]]
            return result

        # Общий случай (метод алгебраических дополнений)
        result = Matrix(self.rows, self.cols)

        # Создаем матрицу алгебраических дополнений
        for i in range(self.rows):
            for j in range(self.cols):
                # Создаем минор, исключая i-ю строку и j-й столбец
                minor = Matrix(self.rows - 1, self.cols - 1)
                row_idx = 0
                for m in range(self.rows):
                    if m == i:
                        continue
                    col_idx = 0
                    for n in range(self.cols):
                        if n == j:
                            continue
                        minor.data[row_idx][col_idx] = self.data[m][n]
                        col_idx += 1
                    row_idx += 1

                # Алгебраическое дополнение
                sign = 1 if (i + j) % 2 == 0 else -1
                result.data[j][i] = sign * minor.determinant() / det

        return result

    def dot_product(self, other):
        """Альтернативное имя для умножения (удобно для ИИ)"""
        return self.multiply(other)

    def hadamard_product(self, other):
        """
        Поэлементное произведение матриц (произведение Адамара)

        Args:
            other (Matrix): Матрица для умножения

        Returns:
            Matrix: Результат поэлементного умножения

        Raises:
            ValueError: Если размеры матриц не совпадают
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Размеры матриц должны совпадать для произведения Адамара")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * other.data[i][j]

        return result

    def apply_function(self, func):
        """
        Применение функции к каждому элементу матрицы

        Args:
            func (callable): Функция для применения

        Returns:
            Matrix: Новая матрица с примененной функцией
        """
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = func(self.data[i][j])

        return result

    def sum(self, axis=None):
        """
        Суммирование элементов матрицы

        Args:
            axis (int, optional): Ось для суммирования (0 - по столбцам, 1 - по строкам, None - все элементы)

        Returns:
            float или Matrix: Результат суммирования
        """
        if axis is None:
            # Сумма всех элементов
            total = 0
            for i in range(self.rows):
                total += sum(self.data[i])
            return total
        elif axis == 0:
            # Сумма по столбцам
            result = Matrix(1, self.cols)
            for j in range(self.cols):
                col_sum = 0
                for i in range(self.rows):
                    col_sum += self.data[i][j]
                result.data[0][j] = col_sum
            return result
        elif axis == 1:
            # Сумма по строкам
            result = Matrix(self.rows, 1)
            for i in range(self.rows):
                row_sum = sum(self.data[i])
                result.data[i][0] = row_sum
            return result
        else:
            raise ValueError("axis должен быть 0, 1 или None")

    def mean(self, axis=None):
        """
        Среднее значение элементов матрицы

        Args:
            axis (int, optional): Ось для вычисления среднего

        Returns:
            float или Matrix: Среднее значение
        """
        if axis is None:
            # Среднее всех элементов
            return self.sum() / (self.rows * self.cols)
        elif axis == 0:
            # Среднее по столбцам
            sums = self.sum(axis=0)
            return sums.scalar_multiply(1 / self.rows)
        elif axis == 1:
            # Среднее по строкам
            sums = self.sum(axis=1)
            return sums.scalar_multiply(1 / self.cols)
        else:
            raise ValueError("axis должен быть 0, 1 или None")

    def copy(self):
        """Создание глубокой копии матрицы"""
        return Matrix(self.rows, self.cols, data=copy.deepcopy(self.data))

    def reshape(self, new_rows, new_cols):
        """
        Изменение формы матрицы

        Args:
            new_rows (int): Новое количество строк
            new_cols (int): Новое количество столбцов

        Returns:
            Matrix: Матрица с новой формой

        Raises:
            ValueError: Если новый размер не соответствует количеству элементов
        """
        if new_rows * new_cols != self.rows * self.cols:
            raise ValueError(
                f"Новая форма должна содержать {self.rows * self.cols} элементов")

        # Собираем все элементы в один список
        elements = []
        for i in range(self.rows):
            elements.extend(self.data[i])

        # Создаем новую матрицу
        result = Matrix(new_rows, new_cols)
        idx = 0
        for i in range(new_rows):
            for j in range(new_cols):
                result.data[i][j] = elements[idx]
                idx += 1

        return result

    @classmethod
    def identity(cls, n):
        """
        Создание единичной матрицы размера n x n

        Args:
            n (int): Размер матрицы

        Returns:
            Matrix: Единичная матрица
        """
        result = cls(n, n)
        for i in range(n):
            result.data[i][i] = 1
        return result

    @classmethod
    def zeros(cls, rows, cols=None):
        """
        Создание матрицы из нулей

        Args:
            rows (int): Количество строк
            cols (int, optional): Количество столбцов

        Returns:
            Matrix: Матрица из нулей
        """
        if cols is None:
            cols = rows
        return cls(rows, cols, fill_value=0)

    @classmethod
    def ones(cls, rows, cols=None):
        """
        Создание матрицы из единиц

        Args:
            rows (int): Количество строк
            cols (int, optional): Количество столбцов

        Returns:
            Matrix: Матрица из единиц
        """
        if cols is None:
            cols = rows
        return cls(rows, cols, fill_value=1)

    @classmethod
    def random(cls, rows, cols=None, low=0.0, high=1.0):
        """
        Создание матрицы со случайными значениями

        Args:
            rows (int): Количество строк
            cols (int, optional): Количество столбцов
            low (float): Нижняя граница случайных значений
            high (float): Верхняя граница случайных значений

        Returns:
            Matrix: Матрица со случайными значениями
        """
        if cols is None:
            cols = rows

        result = cls(rows, cols)
        for i in range(rows):
            for j in range(cols):
                result.data[i][j] = random.uniform(low, high)

        return result

    @classmethod
    def from_list(cls, data):
        """
        Создание матрицы из списка

        Args:
            data (list of list): Данные матрицы

        Returns:
            Matrix: Созданная матрица
        """
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0
        return cls(rows, cols, data=data)


def test_matrix_operations():
    """Тестирование основных операций с матрицами"""

    print("=" * 80)
    print("🧪 ТЕСТИРОВАНИЕ КЛАССА MATRIX ДЛЯ ИИ ЛАБОРАТОРИИ")
    print("=" * 80)

    # Тест 1: Создание и вывод матриц
    print("\n1. 📊 СОЗДАНИЕ И ВЫВОД МАТРИЦ:")

    m1 = Matrix(2, 3, data=[[1, 2, 3], [4, 5, 6]])
    m2 = Matrix(2, 3, data=[[7, 8, 9], [10, 11, 12]])

    print("Матрица 1 (2x3):")
    print(m1)

    print("\nМатрица 2 (2x3):")
    print(m2)

    # Тест 2: Сложение и вычитание
    print("\n" + "=" * 80)
    print("2. ➕➖ СЛОЖЕНИЕ И ВЫЧИТАНИЕ МАТРИЦ:")

    try:
        m_sum = m1.add(m2)
        print("Сложение матриц (m1 + m2):")
        print(m_sum)

        m_diff = m1.subtract(m2)
        print("\nВычитание матриц (m1 - m2):")
        print(m_diff)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 3: Умножение матриц
    print("\n" + "=" * 80)
    print("3. ✖️ УМНОЖЕНИЕ МАТРИЦ:")

    m3 = Matrix(3, 2, data=[[1, 2], [3, 4], [5, 6]])
    print("Матрица 3 (3x2):")
    print(m3)

    try:
        m_product = m1.multiply(m3)
        print("\nУмножение матриц (m1 * m3):")
        print(m_product)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 4: Транспонирование
    print("\n" + "=" * 80)
    print("4. 🔄 ТРАНСПОНИРОВАНИЕ МАТРИЦЫ:")

    m_transposed = m1.transpose()
    print("Транспонирование матрицы 1:")
    print(m_transposed)

    # Тест 5: Определитель и обратная матрица
    print("\n" + "=" * 80)
    print("5. 🧮 ОПРЕДЕЛИТЕЛЬ И ОБРАТНАЯ МАТРИЦА:")

    m4 = Matrix(3, 3, data=[[4, 7, 2], [3, 5, 1], [2, 3, 8]])
    print("Квадратная матрица 4 (3x3):")
    print(m4)

    try:
        det = m4.determinant()
        print(f"\nОпределитель матрицы 4: {det:.2f}")

        if abs(det) > 1e-10:
            m_inverse = m4.inverse()
            print("\nОбратная матрица 4:")
            print(m_inverse)

            # Проверка: A * A⁻¹ = I
            identity_check = m4.multiply(m_inverse)
            print(
                "\nПроверка (A * A⁻¹), должно быть близко к единичной матрице:")
            print(identity_check)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 6: Полезные функции для ИИ
    print("\n" + "=" * 80)
    print("6. 🤖 ФУНКЦИИ ДЛЯ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА:")

    # Случайная матрица для весов нейронной сети
    weights = Matrix.random(3, 4, low=-0.5, high=0.5)
    print("Случайная матрица весов нейронной сети (3x4):")
    print(weights)

    # Применение функции активации (сигмоида)
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    activated = weights.apply_function(sigmoid)
    print("\nПосле применения сигмоидной функции активации:")
    print(activated)

    # Суммирование и усреднение
    print("\nСумма всех элементов:", weights.sum())
    print("Среднее всех элементов:", weights.mean())

    # Сумма по столбцам (batch processing в ИИ)
    col_sums = weights.sum(axis=0)
    print("\nСумма по столбцам (для batch normalization):")
    print(col_sums)

    # Тест 7: Специальные матрицы
    print("\n" + "=" * 80)
    print("7. 🏗️  СПЕЦИАЛЬНЫЕ МАТРИЦЫ:")

    identity = Matrix.identity(3)
    print("Единичная матрица 3x3:")
    print(identity)

    zeros = Matrix.zeros(2, 4)
    print("\nМатрица нулей 2x4:")
    print(zeros)

    ones = Matrix.ones(4, 2)
    print("\nМатрица единиц 4x2:")
    print(ones)

    # Тест 8: Перегрузка операторов
    print("\n" + "=" * 80)
    print("8. ⚡ ПЕРЕГРУЗКА ОПЕРАТОРОВ:")

    print("Использование оператора + (m1 + m2):")
    print(m1 + m2)

    print("\nИспользование оператора - (m1 - m2):")
    print(m1 - m2)

    print("\nИспользование оператора * (m1 * m3):")
    print(m1 * m3)

    print("\nУмножение на скаляр (m1 * 2.5):")
    print(m1 * 2.5)

    # Тест 9: Произведение Адамара
    print("\n" + "=" * 80)
    print("9. ⚗️  ПРОИЗВЕДЕНИЕ АДАМАРА (поэлементное умножение):")

    try:
        hadamard = m1.hadamard_product(m2)
        print("Поэлементное произведение m1 и m2:")
        print(hadamard)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 10: Изменение формы
    print("\n" + "=" * 80)
    print("10. 🎭 ИЗМЕНЕНИЕ ФОРМЫ МАТРИЦЫ:")

    flat_matrix = Matrix(2, 3, data=[[1, 2, 3], [4, 5, 6]])
    print("Исходная матрица 2x3:")
    print(flat_matrix)

    reshaped = flat_matrix.reshape(3, 2)
    print("\nПосле изменения формы на 3x2:")
    print(reshaped)

    print("\n" + "=" * 80)
    print("✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
    print("=" * 80)


def neural_network_example():
    """Пример использования матриц для простой нейронной сети"""

    print("\n" + "=" * 80)
    print("🧠 ПРИМЕР: ПРОСТАЯ НЕЙРОННАЯ СЕТЬ С ИСПОЛЬЗОВАНИЕМ КЛАССА MATRIX")
    print("=" * 80)

    # Симуляция forward propagation в нейронной сети
    # Архитектура: 3 входных нейрона -> 4 скрытых нейрона -> 2 выходных нейрона

    # 1. Входные данные (батч из 2 примеров)
    inputs = Matrix(2, 3, data=[[0.5, 0.3, 0.2], [0.1, 0.4, 0.9]])
    print("1. 📥 ВХОДНЫЕ ДАННЫЕ (2 примера, 3 признака):")
    print(inputs)

    # 2. Веса от входного слоя к скрытому слою (3x4)
    weights_input_hidden = Matrix.random(3, 4, low=-1, high=1)
    print("\n2. ⚖️  ВЕСА ВХОДНОГО СЛОЯ -> СКРЫТЫЙ СЛОЙ (3x4):")
    print(weights_input_hidden)

    # 3. Смещения для скрытого слоя (1x4)
    biases_hidden = Matrix.random(1, 4, low=-0.5, high=0.5)
    print("\n3. ⚖️  СМЕЩЕНИЯ СКРЫТОГО СЛОЯ (1x4):")
    print(biases_hidden)

    # 4. Forward propagation: вычисление выхода скрытого слоя
    # hidden = inputs * weights_input_hidden + biases_hidden
    hidden_pre_activation = inputs.multiply(weights_input_hidden)

    # Добавляем смещения (broadcasting)
    hidden_with_biases = hidden_pre_activation.copy()
    for i in range(hidden_with_biases.rows):
        for j in range(hidden_with_biases.cols):
            hidden_with_biases[i, j] += biases_hidden[0, j]

    print("\n4. 🔄 ВЫХОД СКРЫТОГО СЛОЯ ДО АКТИВАЦИИ (2x4):")
    print(hidden_with_biases)

    # 5. Применение функции активации ReLU
    def relu(x):
        return max(0, x)

    hidden_activated = hidden_with_biases.apply_function(relu)
    print("\n5. ⚡ ВЫХОД СКРЫТОГО СЛОЯ ПОСЛЕ ReLU АКТИВАЦИИ:")
    print(hidden_activated)

    # 6. Веса от скрытого слоя к выходному слою (4x2)
    weights_hidden_output = Matrix.random(4, 2, low=-1, high=1)
    print("\n6. ⚖️  ВЕСА СКРЫТОГО СЛОЯ -> ВЫХОДНОЙ СЛОЙ (4x2):")
    print(weights_hidden_output)

    # 7. Смещения для выходного слоя (1x2)
    biases_output = Matrix.random(1, 2, low=-0.5, high=0.5)
    print("\n7. ⚖️  СМЕЩЕНИЯ ВЫХОДНОГО СЛОЯ (1x2):")
    print(biases_output)

    # 8. Forward propagation: вычисление выхода сети
    output_pre_activation = hidden_activated.multiply(weights_hidden_output)

    # Добавляем смещения
    output_with_biases = output_pre_activation.copy()
    for i in range(output_with_biases.rows):
        for j in range(output_with_biases.cols):
            output_with_biases[i, j] += biases_output[0, j]

    print("\n8. 🔄 ВЫХОД СЕТИ ДО АКТИВАЦИИ (2x2):")
    print(output_with_biases)

    # 9. Применение функции активации Softmax
    def softmax_row(row_data):
        exp_values = [math.exp(x) for x in row_data]
        sum_exp = sum(exp_values)
        return [x / sum_exp for x in exp_values]

    # Применяем softmax к каждой строке отдельно
    output_softmax = Matrix(output_with_biases.rows, output_with_biases.cols)
    for i in range(output_with_biases.rows):
        row_softmax = softmax_row(output_with_biases.data[i])
        output_softmax.data[i] = row_softmax

    print("\n9. 🎯 ВЫХОД СЕТИ ПОСЛЕ SOFTMAX АКТИВАЦИИ (вероятности классов):")
    print(output_softmax)

    print("\n" + "=" * 80)
    print("✅ СИМУЛЯЦИЯ FORWARD PROPAGATION ЗАВЕРШЕНА!")
    print("=" * 80)


def main():
    """Основная функция для демонстрации работы класса Matrix"""

    print("🧪 ЛАБОРАТОРИЯ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА")
    print("📊 КЛАСС MATRIX ДЛЯ ОБРАБОТКИ ДАННЫХ В НЕЙРОННЫХ СЕТЯХ")

    while True:
        print("\n" + "=" * 80)
        print("МЕНЮ ДЕМОНСТРАЦИИ:")
        print("1. 🧪 Запустить полное тестирование операций с матрицами")
        print("2. 🧠 Показать пример использования в нейронной сети")
        print("3. 🎮 Интерактивная работа с матрицами")
        print("4. 🚪 Выход")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == "1":
            test_matrix_operations()
            input("\nНажмите Enter для продолжения...")

        elif choice == "2":
            neural_network_example()
            input("\nНажмите Enter для продолжения...")

        elif choice == "3":
            interactive_matrix_playground()

        elif choice == "4":
            print(
                "\n👋 До свидания! Удачи в исследованиях искусственного интеллекта!")
            break

        else:
            print("❌ Неверный выбор. Пожалуйста, выберите 1-4.")


def interactive_matrix_playground():
    """Интерактивная площадка для работы с матрицами"""

    print("\n" + "=" * 80)
    print("🎮 ИНТЕРАКТИВНАЯ ПЛОЩАДКА ДЛЯ РАБОТЫ С МАТРИЦАМИ")
    print("=" * 80)

    matrices = {}

    while True:
        print(f"\nТекущие матрицы: {list(matrices.keys())}")
        print("\nДоступные операции:")
        print("1. Создать новую матрицу")
        print("2. Показать матрицу")
        print("3. Сложить две матрицы")
        print("4. Вычесть матрицы")
        print("5. Умножить матрицы")
        print("6. Транспонировать матрицу")
        print("7. Вычислить определитель")
        print("8. Найти обратную матрицу")
        print("9. Вернуться в главное меню")

        op_choice = input("\nВыберите операцию (1-9): ").strip()

        if op_choice == "1":
            name = input("Введите имя для матрицы: ").strip()
            rows = int(input("Количество строк: "))
            cols = int(input("Количество столбцов: "))

            print(
                "Введите данные матрицы построчно (числа разделяйте пробелами):")
            data = []
            for i in range(rows):
                while True:
                    row_input = input(f"Строка {i + 1}: ").strip()
                    row_values = row_input.split()
                    if len(row_values) == cols:
                        try:
                            row = [float(x) for x in row_values]
                            data.append(row)
                            break
                        except ValueError:
                            print("Ошибка: введите числа!")
                    else:
                        print(
                            f"Ошибка: нужно {cols} чисел, введено {len(row_values)}")

            matrices[name] = Matrix(rows, cols, data=data)
            print(f"✅ Матрица '{name}' создана!")

        elif op_choice == "2":
            if not matrices:
                print("❌ Нет созданных матриц!")
                continue

            name = input("Введите имя матрицы: ").strip()
            if name in matrices:
                print(f"\nМатрица '{name}':")
                print(matrices[name])
            else:
                print(f"❌ Матрица '{name}' не найдена!")

        elif op_choice in ["3", "4", "5"]:
            if len(matrices) < 2:
                print("❌ Нужно как минимум 2 матрицы!")
                continue

            print("Доступные матрицы:", list(matrices.keys()))
            name1 = input("Имя первой матрицы: ").strip()
            name2 = input("Имя второй матрицы: ").strip()

            if name1 not in matrices or name2 not in matrices:
                print("❌ Одна или обе матрицы не найдены!")
                continue

            try:
                if op_choice == "3":
                    result = matrices[name1] + matrices[name2]
                    print(f"\nРезультат сложения '{name1}' + '{name2}':")
                    print(result)
                elif op_choice == "4":
                    result = matrices[name1] - matrices[name2]
                    print(f"\nРезультат вычитания '{name1}' - '{name2}':")
                    print(result)
                elif op_choice == "5":
                    result = matrices[name1] * matrices[name2]
                    print(f"\nРезультат умножения '{name1}' * '{name2}':")
                    print(result)

                # Предлагаем сохранить результат
                save = input(
                    "\nСохранить результат? (да/нет): ").strip().lower()
                if save in ['да', 'д', 'yes', 'y']:
                    result_name = input("Имя для результата: ").strip()
                    matrices[result_name] = result
                    print(f"✅ Результат сохранен как '{result_name}'")

            except ValueError as e:
                print(f"❌ Ошибка: {e}")
            except TypeError as e:
                print(f"❌ Ошибка: {e}")

        elif op_choice == "6":
            if not matrices:
                print("❌ Нет созданных матриц!")
                continue

            name = input("Введите имя матрицы: ").strip()
            if name in matrices:
                try:
                    result = matrices[name].transpose()
                    print(f"\nТранспонированная матрица '{name}':")
                    print(result)

                    save = input(
                        "\nСохранить результат? (да/нет): ").strip().lower()
                    if save in ['да', 'д', 'yes', 'y']:
                        result_name = input("Имя для результата: ").strip()
                        matrices[result_name] = result
                        print(f"✅ Результат сохранен как '{result_name}'")
                except Exception as e:
                    print(f"❌ Ошибка: {e}")
            else:
                print(f"❌ Матрица '{name}' не найдена!")

        elif op_choice == "7":
            if not matrices:
                print("❌ Нет созданных матриц!")
                continue

            name = input("Введите имя матрицы: ").strip()
            if name in matrices:
                try:
                    det = matrices[name].determinant()
                    print(f"\nОпределитель матрицы '{name}': {det}")
                except ValueError as e:
                    print(f"❌ Ошибка: {e}")
            else:
                print(f"❌ Матрица '{name}' не найдена!")

        elif op_choice == "8":
            if not matrices:
                print("❌ Нет созданных матриц!")
                continue

            name = input("Введите имя матрицы: ").strip()
            if name in matrices:
                try:
                    result = matrices[name].inverse()
                    print(f"\nОбратная матрица для '{name}':")
                    print(result)

                    save = input(
                        "\nСохранить результат? (да/нет): ").strip().lower()
                    if save in ['да', 'д', 'yes', 'y']:
                        result_name = input("Имя для результата: ").strip()
                        matrices[result_name] = result
                        print(f"✅ Результат сохранен как '{result_name}'")
                except ValueError as e:
                    print(f"❌ Ошибка: {e}")
            else:
                print(f"❌ Матрица '{name}' не найдена!")

        elif op_choice == "9":
            break


        else:
            print("❌ Неверный выбор операции!")


if __name__ == "__main__":
    main()

'''2. Расширенные операции для ИИ:
Определитель (determinant): вычисление определителя квадратной матрицы
Обратная матрица (inverse): нахождение обратной матрицы (если существует)
Поэлементное умножение (hadamard_product): произведение Адамара для матриц одинакового размера
Применение функций (apply_function): возможность применять любую функцию к каждому элементу (активации в нейросетях)
Суммирование и усреднение (sum, mean): по всем элементам, по строкам или столбцам

3. Удобные конструкторы:
Matrix.identity(n) - единичная матрица
Matrix.zeros(rows, cols) - матрица нулей
Matrix.ones(rows, cols) - матрица единиц
Matrix.random(rows, cols) - матрица случайных чисел (для инициализации весов)

4. Перегрузка операторов:
+ для сложения
- для вычитания
* для умножения матриц или умножения на скаляр
[] для доступа к элементам
📊 Пример использования (из условия задачи):
🔬 Применение в лаборатории ИИ:
Для нейронных сетей:
python
# Инициализация весов
weights = Matrix.random(3, 4, low=-0.5, high=0.5)
# Forward propagation
inputs = Matrix(2, 3, data=[[0.5, 0.3, 0.2], [0.1, 0.4, 0.9]])
hidden = inputs.multiply(weights)

# Применение функции активации (сигмоида)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

activated = hidden.apply_function(sigmoid)
Для обработки данных:
python
# Нормализация данных
data_matrix = Matrix.from_list(dataset)
mean = data_matrix.mean(axis=0)  # Среднее по столбцам
std = data_matrix.std(axis=0)    # Стандартное отклонение по столбцам
normalized = (data_matrix - mean) / std'''