import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            sleep(0.001)
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
            else:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

    def take(self):
        for i in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")
            sleep(0.001)
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
        self.lock.acquire()

#
bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')