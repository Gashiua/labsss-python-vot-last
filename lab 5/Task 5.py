import matplotlib.pyplot as plt
import numpy as np

# Создаем фигуру с 3 областями (подграфиками)
plt.figure(figsize=(15, 5))  # размер фигуры

# Первый график: линейный y = x^2
plt.subplot(1, 3, 1)  # 1 строка, 3 столбца, первый график
x = np.linspace(0, 10, 100)  # создаем массив x от 0 до 10
y = x ** 2                   # y = x^2
plt.plot(x, y)
plt.title('y = x^2')

# Второй график: точечный scatter
plt.subplot(1, 3, 2)  # второй график
# создаем случайные точки
x_points = np.random.rand(50)
y_points = np.random.rand(50)
plt.scatter(x_points, y_points)
plt.title('Точечный scatter')

# Третий график: столбчатая диаграмма
plt.subplot(1, 3, 3)  # третий график
categories = ['A', 'B', 'C']
values = [5, 4, 1]
plt.bar(categories, values)
plt.title('Столбчатая диаграмма')

# Показываем все графики вместе
plt.tight_layout()  # чтобы не было пересечений
plt.show()