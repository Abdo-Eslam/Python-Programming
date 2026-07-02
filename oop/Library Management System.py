class LibraryBook:
    Books_count = 0
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        if price <= 0:
            print("Invalid Price")
        else:
            self.__price = price
        LibraryBook.Books_count += 1
    
    def display_info(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.__price}")

    def increase_price(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self.__price += amount
    
    def decrease_price(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif self.__price + amount <= 0:
            print("Price can't be negative.")
        else:
            self.__price -= amount

    @property

    def price(self):
        return self.__price
    
    @price.setter

    def price(self, new_price):
        if new_price < 0:
            print("Invalid Price.")
        else:
            self.__price = new_price
    
    @staticmethod

    def library_rules():
        print("Books should be returned within 14 days.")

    @classmethod

    def show_books_count(cls):
        print(f"Total Books = {cls.Books_count}")



book1 = LibraryBook("Clean Code", "Robert Martin", 250)
book2 = LibraryBook("Python Crash Course", "Eric Matthes", 300)
book3 = LibraryBook("Atomic Habits", "James Clear", 200)

print("========== Book 1 ==========")
book1.display_info()

print("\n========== Increase Price ==========")
book1.increase_price(50)
book1.display_info()

print("\n========== Decrease Price ==========")
book1.decrease_price(100)
book1.display_info()

print("\n========== Invalid Increase ==========")
book1.increase_price(-10)

print("\n========== Invalid Decrease ==========")
book1.decrease_price(-20)

print("\n========== Price Can't Be Negative ==========")
book1.decrease_price(1000)

print("\n========== Getter ==========")
print(book1.price)

print("\n========== Setter ==========")
book1.price = 500
print(book1.price)

print("\n========== Invalid Setter ==========")
book1.price = -100

print("\n========== Static Method ==========")
LibraryBook.library_rules()

print("\n========== Class Method ==========")
LibraryBook.show_books_count()