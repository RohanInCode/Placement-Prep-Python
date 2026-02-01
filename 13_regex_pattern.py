# =====================================================
# 🔹 REGEX PATTERNS PRACTICE
# Dot | Anchors | Quantifiers | Sets | Special chars | Groups
# =====================================================

import re



# =====================================================
# 1️⃣ DOT (.)
# matches any single character
# =====================================================

text = "cat cot c@t"
print("Dot:", re.findall("c.t", text))



# =====================================================
# 2️⃣ START ANCHOR (^)
# =====================================================

text = "Hello World"
print("Starts with Hello:", bool(re.search("^Hello", text)))
print("Starts with World:", bool(re.search("^World", text)))



# =====================================================
# 3️⃣ END ANCHOR ($)
# =====================================================

print("Ends with Hello:", bool(re.search("Hello$", text)))
print("Ends with World:", bool(re.search("World$", text)))



# =====================================================
# 4️⃣ + (one or more)
# =====================================================

text = "helloooo"
print("lo+ :", re.findall("lo+", text))



# =====================================================
# 5️⃣ ? (optional)
# =====================================================

text = "color colour"
print("Optional u:", re.findall("colou?r", text))



# =====================================================
# 6️⃣ CHARACTER SET []
# =====================================================

text = "apple ball cat"
print("[abc]:", re.findall("[abc]", text))



# =====================================================
# 7️⃣ DIGITS [0-9]
# =====================================================

text = "My age is 30"
print("Digits:", re.findall("[0-9]", text))



# =====================================================
# 8️⃣ CAPITAL LETTERS
# =====================================================

text = "MY AGe is 40"
print("Caps:", re.findall("[A-Z]", text))



# =====================================================
# 9️⃣ SMALL LETTERS
# =====================================================

text = "you are greAT AT codING"
print("Small:", re.findall("[a-z]", text))



# =====================================================
# 🔟 SPECIAL SHORTCUTS
# =====================================================

text = "Marks: 90"

print("\\d (digits):", re.findall(r"\d", text))
print("\\D (non-digits):", re.findall(r"\D", text))
print("\\w (word chars):", re.findall(r"\w", text))
print("\\W (non-word):", re.findall(r"\W", text))
print("\\s (space):", re.findall(r"\s", text))
print("\\S (non-space):", re.findall(r"\S", text))



# =====================================================
# 1️⃣1️⃣ QUANTIFIER {n}
# =====================================================

text = "Phone: 7993141314"
print("10 digits:", re.findall(r"\d{10}", text))



# =====================================================
# 1️⃣2️⃣ OR OPERATOR (|)
# =====================================================

text = "I have a cat and a dog"
print("OR:", re.findall("cat|dog", text))



# =====================================================
# 1️⃣3️⃣ GROUPING ()
# =====================================================

text = "abab ab"
print("Grouping:", re.findall("(ab)+", text))
