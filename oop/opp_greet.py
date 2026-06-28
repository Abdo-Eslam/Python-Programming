class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(
            f"Hello, my name is {self.name} and i am {self.age} years old."
        )

person1 = person("Tom", 23)
person1.greet()

person2 = person("Alison", 42)
person2.greet()