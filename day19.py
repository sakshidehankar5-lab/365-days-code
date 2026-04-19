#1st program
class Student:
    def __init__(self, name, marks):
        self.name = name          # public variable
        self.__marks = marks      # private variable

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

# object creation
s1 = Student("Rahul", 85)

print(s1.name)            # accessible
print(s1.get_marks())     # accessing private variable using getter

s1.set_marks(90)          # modifying using setter
print(s1.get_marks())









#2nd program
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)

acc.deposit(500)
print(acc.get_balance())

# print(acc.__balance)  # This will give error