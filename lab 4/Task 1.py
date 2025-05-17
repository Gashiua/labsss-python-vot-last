import random
import time

# Функция для игры
def play_game():
    number = random.randint(1, 50)  # загадываем число от 1 до 100
    attempts = 0
    start_time = time.time()  # время начала игры

    print("Здарова ,студент!Я сейчас число загадаю от 1 до 50,а ты попробуй угадать!")

    while True:
        guess = input("Погнали ,друг!Введи число: ")
        attempts += 1

        # Проверяем, что пользователь ввел число
        if not guess.isdigit():
            print("Не,так не пойдет!Вводи число давай!")
            continue

        guess_number = int(guess)

        if guess_number == number:
            print(f"Вот это да!Ты угадал число {number} за {attempts} попыток!Сильно!")
            break
        elif guess_number < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    end_time = time.time()  # время конца игры
    total_time = end_time - start_time

    # Сохраняем статистику в файл
    with open("statistics.txt", "a") as file:
        file.write(f"Попытки: {attempts}, Время: {total_time:.2f} сек, Результат: Угадано\n")

# Запускаем игру
play_game()