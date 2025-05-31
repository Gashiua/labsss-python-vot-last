def print_board(cells):
    print("Текущая доска:")
    for i in range(3):
        row = []
        for j in range(3):
            index = i * 3 + j + 1
            cell_value = cells[index]
            row.append(cell_value)
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(cells, mark):
    # Все выигрышные комбинации по номерам ячеек
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # строки
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # столбцы
        [1, 5, 9], [3, 5, 7]             # диагонали
    ]
    for combo in winning_combinations:
        if all(cells[pos] == mark for pos in combo):
            return True
    return False

def is_full(cells):
    # Проверка заполненности всех ячеек (если все заняты X или O)
    return all(cells[i] != str(i) for i in range(1,10))

def main():
    # Инициализация доски номерами
    cells = {i: str(i) for i in range(1,10)}
    current_player = "X"

    while True:
        print_board(cells)
        print(f"Ходит игрок {current_player}")
        try:
            move = int(input("Введите номер ячейки (1-9): "))
            if move not in range(1,10):
                print("Некорректный номер. Попробуйте снова.")
                continue
            if cells[move] in ["X", "O"]:
                print("Эта ячейка уже занята. Попробуйте другую.")
                continue

            # Занимаем ячейку
            cells[move] = current_player

            # Проверка победы
            if check_winner(cells, current_player):
                print_board(cells)
                print(f"Поздравляем! Игрок {current_player} победил!")
                break

            # Проверка ничьи
            if is_full(cells):
                print_board(cells)
                print("Ничья!")
                break

            # Меняем игрока
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Пожалуйста, вводите числа.")

if __name__ == "__main__":
    main()
