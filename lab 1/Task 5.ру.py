import random

# Генерируем список из 20 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(20)]

# Выводим сгенерированный список
print("Сгенерированный список чисел:", numbers)

# Находим все чётные числа из списка
even_numbers = [num for num in numbers if num % 2 == 0]
print("Все чётные числа из списка:", even_numbers)

# Находим все числа, которые растут на 3
growing_by_3 = [num for i, num in enumerate(numbers[:-1]) if numbers[i + 1] - num == 3]
print("Все числа, которые растут на 3:", growing_by_3)

# Вычисляем ср.арифметическое всех чисел в списке
average = sum(numbers) / len(numbers)
print("Среднее арифметическое всех чисел в списке:", average)