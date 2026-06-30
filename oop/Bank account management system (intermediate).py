class bankaccount:
    def __init__(self, owner, balance, email):
        self.owner = owner
        self.__balance = balance
        self._email = email

    def get_mail(self):
        print(f"the emil is {self._email}")

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            print("has been modified")    

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
        print(f"owner:{self.owner} \nbalance:{self.__balance}")

        self._bank_message()
        self.__secret_code()


acc1 = bankaccount("Ahmed", 5000, "ahmed@gmail.com")

acc1.show_balance()
acc1.get_mail()

acc1.deposit(1000)
acc1.withdraw(1500)

acc1.show_balance()

acc1.deposit(-50)
acc1.withdraw(10000)


acc1.set_email("abdo@gmail.com")

acc1.get_mail()