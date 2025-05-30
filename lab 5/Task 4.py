import numpy as np
import matplotlib.pyplot as plt

# Создаем матрицу 5x5 со случайными числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

# Строим тепловую карту
plt.imshow(matrix, cmap='viridis')  # 'viridis' — цветовая схема

# Добавляем цветовую шкалу справа
plt.colorbar()

# Добавляем числа в каждую ячейку
for i in range(5):
    for j in range(5):
        plt.text(j, i, str(matrix[i][j]), ha='center', va='center', color='white')

# Показываем картинку
plt.title('Тепловая карта матрицы')
plt.show()