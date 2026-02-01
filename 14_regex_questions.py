# =====================================================
# 🔹 REGEX PRACTICE QUESTIONS
# Each section = Question + Solution
# =====================================================

import re



# =====================================================
# Q1. Match any 3-letter word starting with 'c' and ending with 't'
# Pattern: .
# =====================================================
text = "cat cot c@t"
print("Q1:", re.findall("c.t", text))



# =====================================================
# Q2. Check if string starts with "Hello"
# Pattern: ^
# =====================================================
text = "Hello World"
print("Q2:", bool(re.search("^Hello", text)))



# =====================================================
# Q3. Check if string ends with "World"
# Pattern: $
# =====================================================
print("Q3:", bool(re.search("World$", text)))



# =====================================================
# Q4. Match 'lo' followed by one or more 'o'
# Pattern: +
# =====================================================
text = "helloooo"
print("Q4:", re.findall("lo+", text))



# =====================================================
# Q5. Match both color and colour
# Pattern: ?
# =====================================================
text = "color colour"
print("Q5:", re.findall("colou?r", text))



# =====================================================
# Q6. Find only letters a, b, c
# Pattern: []
# =====================================================
text = "apple ball cat"
print("Q6:", re.findall("[abc]", text))



# =====================================================
# Q7. Extract digits from string
# Pattern: [0-9]
# =====================================================
text = "My age is 30"
print("Q7:", re.findall("[0-9]", text))



# =====================================================
# Q8. Extract capital letters
# =====================================================
text = "MY AGe is 40"
print("Q8:", re.findall("[A-Z]", text))



# =====================================================
# Q9. Extract small letters
# =====================================================
text = "you are greAT AT codING"
print("Q9:", re.findall("[a-z]", text))



# =====================================================
# Q10. Use shortcuts (\d \w \s etc)
# =====================================================
text = "Marks: 90"

print("Q10 digits:", re.findall(r"\d", text))
print("Q10 words:", re.findall(r"\w", text))
print("Q10 spaces:", re.findall(r"\s", text))



# =====================================================
# Q11. Extract exactly 10-digit mobile number
# Pattern: {n}
# =====================================================
text = "Phone: 7993141314"
print("Q11:", re.findall(r"\d{10}", text))



# =====================================================
# Q12. Match cat OR dog
# Pattern: |
# =====================================================
text = "I have a cat and a dog"
print("Q12:", re.findall("cat|dog", text))



# =====================================================
# Q13. Match repeated group 'ab'
# Pattern: ()
# =====================================================
text = "abab ab"
print("Q13:", re.findall("(ab)+", text))
