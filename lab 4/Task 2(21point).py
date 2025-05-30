import random

def main():
    print("Игра '21 очко' — упрощённый Блэкджек.")
    
    # Начинаем игру
    # Игрок получает 2 случайных карты (от 2 до 11)
    player_cards = [random.randint(2, 11) for _ in range(2)]
    player_sum = sum(player_cards)
    
    # Дилер получает одну карту
    dealer_card = random.randint(2, 11)
    
    print(f"Ваши карты: {player_cards} (сумма: {player_sum})")
    print(f"Карта дилера: {dealer_card}")
    
    # Ход игрока
    while True:
        choice = input("Хотите взять ещё карту? (да/нет): ").lower()
        if choice == "да":
            new_card = random.randint(2, 11)
            player_cards.append(new_card)
            player_sum += new_card
            print(f"Вам выпала карта: {new_card}")
            print(f"Ваши карты: {player_cards} (сумма: {player_sum})")
            if player_sum > 21:
                print("Перебор! Вы проиграли.")
                return
        elif choice == "нет":
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
    
    # Ход дилера
    dealer_cards = [dealer_card]
    dealer_sum = dealer_card
    
    while dealer_sum < 17:
        new_card = random.randint(2, 11)
        dealer_cards.append(new_card)
        dealer_sum += new_card
    
    print(f"Карты дилера: {dealer_cards} (сумма: {dealer_sum})")
    
    
    if dealer_sum > 21:
        print("Дилер перебрал! Вы победили!")
    elif dealer_sum == player_sum:
        print("Ничья!")
    elif player_sum > dealer_sum:
        print("Вы победили!")
    else:
        print("Вы проиграли!")

main()