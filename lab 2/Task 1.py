import random

# Шаг 1: Создаем файл data.txt с 10 случайными числами
with open('data.txt', 'w') as file:
    for _ in range(10):
        number = random.randint(1, 100)  
        file.write(f"{number}\n")  # Записываем число в файл, каждое на новой строке

# Шаг 2: Читаем числа из файла и рассчитываем статистику
with open('data.txt', 'r') as file:
    numbers = []  # Создаем пустой список для хранения чисел
    for line in file:  # Читаем файл построчно
        number = int(line.strip())  # Преобразуем строку в целое число
        numbers.append(number)  # Добавляем число в список

# Рассчитываем сумму, среднее, максимум и минимум
total_sum = sum(numbers)  
average = total_sum / len(numbers)
maximum = max(numbers) 
minimum = min(numbers) 
# Сохраняем результаты в result.txt
with open('result.txt', 'w') as result_file:
    result_file.write(f"Сумма: {total_sum}\n")  
    result_file.write(f"Среднее: {average:.2f}\n")  
    result_file.write(f"Максимум: {maximum}\n")  
    result_file.write(f"Минимум: {minimum}\n")  