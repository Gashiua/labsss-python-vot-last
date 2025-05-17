# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Деление первого числа на второе с обработкой деления на ноль."""
    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b