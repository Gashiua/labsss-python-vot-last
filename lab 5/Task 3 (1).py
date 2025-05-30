import numpy as np

# Создаем матрицу 5x5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

# Выводим матрицу
print("Матрица:")
print(matrix)

# Находим среднее значение всех элементов
average = np.mean(matrix)
print("Среднее значение:", average)

# Находим максимальный элемент
max_value = np.max(matrix)
print("Максимальный элемент:", max_value)

# Находим минимальный элемент
min_value = np.min(matrix)
print("Минимальный элемент:", min_value)

# Находим сумму по каждому столбцу
sum_columns = np.sum(matrix, axis=0)
print("Сумма по столбцам:", sum_columns)