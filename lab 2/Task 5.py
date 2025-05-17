# Создаем список чисел от 1 до 20
numbers = list(range(1, 21))
print("Список чисел от 1 до 20:", numbers)

# Отфильтруем только чётные числа (используем лямбда-функцию с filter)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Чётные числа:", even_numbers)

# Увеличим каждое число на 10 (используем лямбда-функцию с map)
plus_ten = list(map(lambda x: x + 10, even_numbers))
print("После прибавления 10 к каждому числу:", plus_ten)

# Отсортируем по убыванию (используем sorted с параметром reverse=True)
sorted_desc = sorted(plus_ten, reverse=True)
print("Отсортировано по убыванию:", sorted_desc)