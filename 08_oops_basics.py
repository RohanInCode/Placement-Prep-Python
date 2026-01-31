# =====================================================
# 🔹 OOP BASICS – CONSTRUCTORS / VARIABLES / METHODS
# =====================================================


# =====================================================
# 1️⃣ SIMPLE CONSTRUCTOR
# =====================================================

class Student:
    def __init__(self):
        self.name = "Rahul"

s1 = Student()
print(s1.name)



# =====================================================
# 2️⃣ PARAMETERIZED CONSTRUCTOR
# =====================================================

class Student:
    def __init__(self, fullname):
        self.name = fullname

s2 = Student("Rohan")
print(s2.name)



# =====================================================
# 3️⃣ MULTIPLE PARAMETERS
# =====================================================

class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

s3 = Student("Rohan", 90)
print(s3.name, s3.marks)



# =====================================================
# 4️⃣ CLASS VARIABLE EXAMPLE
# =====================================================

class Student:
    collegename = "LPU"   # class variable

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

s4 = Student("Rohan", 79)
print(s4.collegename)



# =====================================================
# 5️⃣ EMPLOYEE CLASS
# =====================================================

class Employee:
    companyname = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Rohan", 40000)
print(e1.name, e1.salary, e1.companyname)



# =====================================================
# 6️⃣ OBJECT METHOD
# =====================================================

class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Welcome", self.name)

s5 = Student("Karan")
s5.hello()



# =====================================================
# 7️⃣ STATIC METHOD
# =====================================================

class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def collegename():
        print("This is LPU")

Student.collegename()



# =====================================================
# 8️⃣ OBJECT COUNTER (CLASS VARIABLE INCREMENT)
# =====================================================

class Student:
    stcount = 0

    def __init__(self, name):
        self.name = name
        Student.stcount += 1

s6 = Student("Rohan")
s7 = Student("Akmal")

print("Total students:", Student.stcount)



# =====================================================
# 🔒 ENCAPSULATION EXAMPLES
# =====================================================


# =====================================================
# 9️⃣ PRIVATE VARIABLE + GETTER
# =====================================================

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s8 = Student(80)
print(s8.get_marks())



# =====================================================
# 🔟 GETTER + SETTER
# =====================================================

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        self.__marks = new_marks

s9 = Student(100)
s9.set_marks(90)
print(s9.get_marks())



# =====================================================
# 1️⃣1️⃣ BANK CLASS (ENCAPSULATION)
# =====================================================

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

b1 = Bank(80000)
b1.set_balance(2000000)
print(b1.get_balance())



# =====================================================
# 1️⃣2️⃣ BANK ACCOUNT MINI PROJECT
# =====================================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


acc = BankAccount(5000)

acc.deposit(2000)
acc.withdraw(1000)

print("Final balance:", acc.get_balance())
 


