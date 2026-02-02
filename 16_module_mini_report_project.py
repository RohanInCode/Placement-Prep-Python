# =====================================================
# 🔹 MINI REPORT GENERATOR PROJECT
# Uses: random | math | Counter | os
# =====================================================

import random
import os
import math
from collections import Counter


# =====================================================
# 1️⃣ Generate random numbers
# =====================================================

numbers = [random.randint(1, 10) for _ in range(10)]
print("Numbers:", numbers)


# =====================================================
# 2️⃣ Separate even and odd numbers
# =====================================================

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


# =====================================================
# 3️⃣ Calculate average
# =====================================================

average = sum(numbers) / len(numbers)


# =====================================================
# 4️⃣ Round off average
# =====================================================

rounded_avg = math.ceil(average)


# =====================================================
# 5️⃣ Count frequency
# =====================================================

count_numbers = Counter(numbers)


# =====================================================
# 6️⃣ Save results using OS + file handling
# =====================================================

folder_name = "easy_reports"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

file_path = os.path.join(folder_name, "report.txt")

with open(file_path, "w") as file:
    file.write("===== NUMBER REPORT =====\n")
    file.write(f"Numbers: {numbers}\n")
    file.write(f"Even Numbers: {even_numbers}\n")
    file.write(f"Odd Numbers: {odd_numbers}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Rounded Average: {rounded_avg}\n")
    file.write(f"Frequency Count: {count_numbers}\n")

print("\nReport saved at:", file_path)
