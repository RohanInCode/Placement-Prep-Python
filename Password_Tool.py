import re
import os 


# Step 1: Take password input from user
Pass = input("Enter the password:")

# Step 2: Find total number of characters
char_len = len(Pass)


# Step 3: Regex patterns to check lowercase, uppercase, digits and symbols
patterns = [r'[a-z]', r'[A-Z]', r'[0-9]', r'[^A-Za-z0-9]']


# Step 4: Count how many character types are present
types = 0
for p in patterns:
    if re.search(p, Pass):
        types += 1


# Step 5: Calculate strength score using types × length
score = (types * char_len)


# Step 6: Decide password strength based on score
if score < 10:
    strength = "Weak"
elif score < 25:
    strength = "Medium"
else:
    strength = "Strong"

print("Strength:", strength)


# Step 7: Create folder if not exists
if not os.path.exists("results"):
    os.mkdir("results")


# Step 8: Open file and save results
file = open("result.txt", "w")

file.write("Password: " + Pass + "\n")
file.write("Length: " + str(char_len) + "\n")
file.write("Types: " + str(types) + "\n")
file.write("Score: " + str(score) + "\n")
file.write("Strength: " + strength + "\n")


# Step 9: Close file
file.close()


