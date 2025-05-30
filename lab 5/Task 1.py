%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

# Создаем массив x от 0 до 10 с 100 точками
x = np.linspace(0, 10, 100)

# Вычисляем y = sin(x) и z = cos(x)
y = np.sin(x)
z = np.cos(x)

# Строим два графика на одном графике
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')

# Добавляем легенду
plt.legend()

# Подписываем оси
plt.xlabel('Ось х')
plt.ylabel('Значение функции')

# Добавляем заголовок
plt.title('Графики sin(x) и cos(x)')

