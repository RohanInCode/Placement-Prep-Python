# =========================================================
# 🔹 INPUT + IF ELSE
# =========================================================

c = int(input("Enter the number: "))
b = int(input("Enter the number: "))
if c > b :
    print("c is greater")
elif b > c:
    print("b is greater")
else :
    print("no number is greater")



# =========================================================
# 🔹 TRAFFIC SIGNAL
# =========================================================


color = str(input("Enter the light: "))
 
if color == "red" :
    print("you should stop ")
elif color == "orange":
    print("wait")
elif color == "green" :
    print("You are ready to go")
else :
    print("invalid")



# =========================================================
# 🔹 FOR LOOP (ODD NUMBERS)
# =========================================================


a = 15
for i in range (a) :
    if i % 2 != 0:
        print(i)

for i in range (1,16) :
    if i % 2 != 0:
        print(i) 


# Star pattern


for i in range(1, 6):
    print("*" * i)


# =========================================================
# 🔹 WHILE LOOP (TABLE)
# =========================================================


num = int(input("Enter the number: "))
i = 1
while (i<=10):
    print(num ,"x" ,i , "=", num*i)
    i += 1



# =========================================================
# 🔹 FUNCTIONS + LAMBDA
# =========================================================


def sum(a,b):
    return a + b

addition = sum (5,6)
print (addition)

def add(a,b):
    print(a + b)
    
add(10,20)

add = lambda x,y:(x + y)
print(add(10,20))

sqrt = lambda x: int(x ** 0.5)
print(sqrt(16))
