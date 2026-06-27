
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def add_fees(self, fees):
        self.price = self.price + fees
        print(f"The total price after fees is: {self.price}")


class User:
    def __init__(self, username, email, points, product):
        self.username = username
        self.email = email
        self.points = points
        self.product = product

    def add_points(self, amount):
        self.points = self.points + amount
        print(f"User {self.username}, your new credit is: {self.points}")



product1 = Product("BOOK", 100)
user1 = User("abdo123", "abdo34@gmail.com", points=100, product=product1)

print(user1.username)
print(user1.email)
user1.add_points(300)


print(user1.product.name)
user1.product.add_fees(10)