class bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
    
    def show_balance(self):
        print(
            f"{self.owner}'s balance is {self.__balance} "
        )

    def _bank_message(self):
        print("Thank you for banking with us.")

    def __secret_code(self):
        print("Bank Internal Code")

    def show_account_info(self):
        print(f"owner:{self.owner} \n balance:{self.__balance}")

        self._bank_message()
        self.__secret_code()


acc1 = bankaccount("Ahmed", 5000)

acc1.show_balance()

acc1.deposit(1000)
acc1.withdraw(1500)

acc1.show_balance()

acc1.deposit(-50)
acc1.withdraw(10000)

print(acc1.owner)        