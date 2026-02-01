# =====================================================
# 🔹 COMPOSITION PRACTICE – HAS-A RELATIONSHIP
# =====================================================
# Composition means:
# One class contains an object of another class
# Example: Student HAS-A Address
# =====================================================



# =====================================================
# 1️⃣ ADDRESS CLASS
# =====================================================

class Address:
    def __init__(self, city):
        self.city = city

    def show_address(self):
        print("City:", self.city)



# =====================================================
# 2️⃣ STUDENT CLASS (COMPOSITION)
# =====================================================

class Student:
    def __init__(self, name, city):
        self.name = name

        # Composition:
        # Creating object of Address inside Student
        self.address = Address(city)

    def show_student(self):
        print("Name:", self.name)

        # Using method of another class
        self.address.show_address()



# =====================================================
# 3️⃣ DRIVER CODE
# =====================================================

print("\n--- Composition Demo ---")

s = Student("Rohan", "Hyderabad")
s.show_student()


        