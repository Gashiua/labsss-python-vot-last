# main.py

# Импортируем функции из модуля math_operations
from math_operations import add, subtract, multiply, divide

# Демонстрация работы функций
a = 20
b = 5

print(f"Сложение {a} + {b} = {add(a, b)}")         
print(f"Вычитание {a} - {b} = {subtract(a, b)}")   
print(f"Умножение {a} * {b} = {multiply(a, b)}")   
print(f"Деление {a} / {b} = {divide(a, b)}")       

# Пример деления на ноль
print(f"Деление {a} / 0 = {divide(a, 0)}")          # Деление на ноль