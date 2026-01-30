# =========================================================
# 🔹 STRING METHODS
# =========================================================

'''
s = "python programming"
print(len(s))
print(s[-1])
print(s[:4])
print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("python" , "java"))
print(s[::-1])
'''


# =========================================================
# 🔹 PALINDROME
# =========================================================

'''
a = "madam"
rev = (a[::-1])

if a == rev:
    print("Its a palindrome")
else:
    print("Its not")
'''


# =========================================================
# 🔹 COUNT VOWELS
# =========================================================

'''
s = "rohan"
count = 0
for i in s :
    if i in "aeiou":
        count +=1
        
print(count)
'''


# =========================================================
# 🔹 REPLACE VOWELS
# =========================================================

'''
s = "pythn"
result=""
for ch in s:
    if ch in "aeiou":
        result += "*"
    else:
        result += ch 
print(result)
'''
