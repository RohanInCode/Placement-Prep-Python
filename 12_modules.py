# =====================================================
# 🔹 PYTHON BUILT-IN MODULES PRACTICE
# math | random | datetime | collections | os
# =====================================================



# =====================================================
# 1️⃣ MATH MODULE
# =====================================================

import math

num = 16

print("Square root:", math.sqrt(num))
print("Power 2^3:", math.pow(2, 3))
print("Floor:", math.floor(7.8))
print("Ceil:", math.ceil(7.8))
print("Absolute:", math.fabs(-5))



# =====================================================
# 2️⃣ RANDOM MODULE
# =====================================================

import random

print("\n--- Random Demo ---")

dice = random.randint(1, 10)
print("Dice:", dice)

students = ["Rahul", "Karan", "Vishal", "Neha"]
selected = random.choice(students)
print("Selected student:", selected)

otp = random.randint(1000, 9999)
print("OTP:", otp)



# =====================================================
# 3️⃣ DATETIME MODULE
# =====================================================

import datetime

print("\n--- DateTime Demo ---")

current = datetime.datetime.now()
print("Current DateTime:", current)

today = datetime.date.today()
print("Today:", today)

date1 = datetime.date(2026, 1, 1)
date2 = datetime.date(2026, 1, 29)

diff = date2 - date1
print("Days difference:", diff)



# =====================================================
# 4️⃣ COLLECTIONS MODULE (Counter)
# =====================================================

from collections import Counter

fruits = [
    "banana", "apple", "pineapple", "mango",
    "banana", "apple", "banana"
]

count = Counter(fruits)
print("\nFruit Count:", count)



# =====================================================
# 5️⃣ STRING SPLIT EXAMPLE
# =====================================================

sentence = "Python is easy and python is powerful"
words = sentence.split()
print("Words:", words)



# =====================================================
# 6️⃣ OS MODULE (FILES & FOLDERS)
# =====================================================

import os

print("\n--- OS Demo ---")

current_path = os.getcwd()
print("Current path:", current_path)

items = os.listdir()
print("Items in folder:", items)


# Create folder if not exists
folder_name = "My_Folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder Created Successfully")
else:
    print("Folder is already present")
