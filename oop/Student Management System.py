class Student:
    def __init__(self, name, age, grade):
        self.name = name
        if age < 10:
            self._age = 0
        else:
            self._age = age

        if grade < 0:
            self.__grade = 0
        else:
            self.__grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Grade: {self.__grade}")

    def increase_grade(self, points):
        if points <= 0:
            print("Invalid points.")
        else:
            self.__grade += points

    def decrease_grade(self, points):
        if points <= 0:
            print("Invalid points.")
        elif self.__grade - points < 0:
            print("Grade can't be negative.")
        else:
            self.__grade -= points

    def is_passed(self):
        if self.__grade >= 50:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")

    def _school_message(self):
        print("Keep learning every day!")

    def __student_id(self):
        print("Student ID Verified.")

    def report(self):
        self.display_info()
        self.is_passed()
        self._school_message()
        self.__student_id()


student_1 = Student("Ahmed", 19, 40)
student_2 = Student("Ali", 20, 85)

print("========== Student 1 ==========")
student_1.report()

print("\n========== Student 2 ==========")
student_2.report()

print("\n========== Increase Grade ==========")
student_1.increase_grade(20)
student_1.report()

print("\n========== Invalid Increase ==========")
student_1.increase_grade(-10)

print("\n========== Decrease Grade ==========")
student_2.decrease_grade(30)
student_2.report()

print("\n========== Invalid Decrease ==========")
student_2.decrease_grade(-5)

print("\n========== Grade Can't Be Negative ==========")
student_1.decrease_grade(1000)

print("\n========== Public Attribute ==========")
print(student_1.name)

print("\n========== Protected Attribute ==========")
print(student_1._age)

print("\n========== Protected Method ==========")
student_1._school_message()

