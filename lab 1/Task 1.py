import random 

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)

# Выводим сгенерированные числа
print("Сгенерированные числа:", num1, num2, num3)

# Находим наибольшее число
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# Находим наименьшее число
if num1 <= num2 and num1 <= num3:
    min_num = num1
elif num2 <= num1 and num2 <= num3:
    min_num = num2
else:
    min_num = num3

# Проверяем, равны ли все три числа
if num1 == num2 and num2 == num3:
    all_equal = True
else:
    all_equal = False

print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)
print("Все числа равны?", all_equal)