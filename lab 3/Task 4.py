class BankAccount:
    def __init__(self):
        self.__balance = 0  # приватный атрибут баланса
        self.__transactions = []  # приватный список транзакций

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit: {amount}")
        else:
            print("Нельзя внести отрицательную сумму!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append(f"Withdraw: {amount}")
            else:
                print("Недостаточно денег на счёте!")
        else:
            print("Нельзя снять отрицательную сумму!")

    @property
    def balance(self):
        return self.__balance

# Пример
account = BankAccount()
account.deposit(100)
account.withdraw(87)
print("Баланс:", account.balance)