import random

numbers = []


for i in range(10):
    num = random.randint(1, 100)  
    numbers.append(num)  # Добавляем сгенерированное число в список

print("Список:", numbers)


max_value = max(numbers)


min_value = min(numbers)
print("Максимальное значение:", max_value)
print("Минимальное значение:", min_value)

total_sum = sum(numbers)
print("Сумма элементов списка:", total_sum)

# Сортируем список по возрастанию
numbers.sort()

# Выводим отсортированный список на экран
print("Отсортированный список:", numbers)