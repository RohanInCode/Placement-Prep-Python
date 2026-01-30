# =====================================================
# 🔹 EXCEPTION HANDLING PRACTICE
# =====================================================

# File handling error


try:
    f = open("movies.txt")
except:
    print("file not found error")
finally:
    print("program finished")



# Raise error manually


age = 20
if age < 18:
    raise ValueError("Age must be 18 or above")
print("Eligible to vote")



# Custom Exception


class LowBalanceError(Exception):
    pass

balance = 500
withdraw = 700

try:
    if withdraw > balance:
        raise LowBalanceError("Insufficient balance")
except LowBalanceError as e:
    print(e)


# Division error


try:
    num = int(input("Enter number: "))
    print(100/num)
except ValueError:
    print("Invalid input")
except:
    print("Error occurred")


# Finally return behavior


def test():
    try:
        return 10
    finally:
        return 20

print(test())

