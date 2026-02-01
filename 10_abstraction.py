# =====================================================
# 🔹 ABSTRACTION PRACTICE – INTERFACE STYLE DESIGN
# =====================================================
# Parent class only defines structure (methods with pass)
# Child classes implement the actual behavior
# =====================================================



# =====================================================
# 1️⃣ PAYMENT SYSTEM (ABSTRACTION)
# =====================================================

class Payment:
    def pay(self, amount):
        pass


class Upi(Payment):
    def pay(self, amount):
        print("Paid using UPI:", amount)


class Cash(Payment):
    def pay(self, amount):
        print("Paid using Cash:", amount)


class Card(Payment):
    def pay(self, amount):
        print("Paid using Card:", amount)


print("\n--- Payment Demo ---")
Upi().pay(12)
Cash().pay(20)
Card().pay(2000)



# =====================================================
# 2️⃣ SHAPES DRAWING (ABSTRACTION)
# =====================================================

class Shape:
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        print("Draw a Square")


class Circle(Shape):
    def draw(self):
        print("Draw a Circle")


class Triangle(Shape):
    def draw(self):
        print("Draw a Triangle")


print("\n--- Shapes Demo ---")
Square().draw()
Circle().draw()
Triangle().draw()



# =====================================================
# 3️⃣ SIMPLE NAME INTERFACE
# =====================================================

class Name:
    def show(self, n):
        pass


class Child(Name):
    def show(self, n):
        print("Name is:", n)


print("\n--- Name Demo ---")
Child().show("Rohan")



# =====================================================
# 4️⃣ MULTIPLE ABSTRACTION (COURSE + EXAM INTERFACE)
# =====================================================

class Course:
    def course_info(self):
        print("This is a programming course")

    def duration(self):
        pass


class ExamInterface:
    def examtype(self):
        pass


class Python(Course, ExamInterface):
    def duration(self):
        print("8 Hour")

    def examtype(self):
        print("Exam is practical based")


print("\n--- Course Demo ---")
obj = Python()
obj.course_info()
obj.duration()
obj.examtype()
