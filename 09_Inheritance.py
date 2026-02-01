# =====================================================
# 🔹 INHERITANCE PRACTICE – SINGLE / MULTIPLE / OVERRIDING
# =====================================================


# =====================================================
# 1️⃣ SINGLE INHERITANCE
# =====================================================

class Human:
    def eat(self):
        print("Human can eat")


class Student(Human):
    def study(self):
        print("Student can study")


print("\n--- Single Inheritance ---")
s = Student()
s.study()
s.eat()



# =====================================================
# 2️⃣ MULTILEVEL INHERITANCE
# =====================================================

class Nokia:
    def call(self):
        print("Can make calls")

class Smartphone(Nokia):
    def sms(self):
        print("Can send SMS")

class Iphone(Smartphone):
    def internet(self):
        print("Can use internet")


p = Iphone()
p.call()       # from Nokia
p.sms()        # from Smartphone
p.internet()   # from Iphone




# =====================================================
# 3️⃣ CONSTRUCTOR INHERITANCE (super)
# =====================================================

class Parent:
    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")


print("\n--- Constructor Inheritance ---")
Child()



# =====================================================
# 4️⃣ METHOD OVERRIDING
# =====================================================

class Parent:
    def work(self):
        print("Go to office")


class Child(Parent):
    def work(self):
        print("Go to school")


print("\n--- Method Overriding ---")
Child().work()



# =====================================================
# 5️⃣ MULTIPLE INHERITANCE
# =====================================================

class Teacher:
    def teach(self):
        print("Teacher teaches")


class Coder:
    def code(self):
        print("Coder codes")


class Student(Teacher, Coder):
    pass


print("\n--- Multiple Inheritance ---")
obj = Student()
obj.teach()
obj.code()



# =====================================================
# 6️⃣ super() WITH PARENT METHOD
# =====================================================

class Shape:
    def draw(self):
        print("Square")


class Circle(Shape):
    def draw(self):
        print("Circle")
        super().draw()


print("\n--- super() Example ---")
Circle().draw()



# =====================================================
# 7️⃣ PRIVATE VARIABLE (NAME MANGLING)
# =====================================================

class Parent:
    def __init__(self):
        self.__x = 10   # private


class Child(Parent):
    def show(self):
        print(self._Parent__x)   # accessing private safely


print("\n--- Private Variable Access ---")
Child().show()



# =====================================================
# 8️⃣ ENCAPSULATION + INHERITANCE
# =====================================================

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Student(Person):
    def show_name(self):
        print("My name is", self.get_name())


print("\n--- Encapsulation + Inheritance ---")
Student("Rohan").show_name()
