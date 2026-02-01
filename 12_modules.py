# import math
# num = 16
# print(math.sqrt(num)) # Square Root 

# num = 16
# result = math.sqrt(num)
# print("Square root of num:",result) #Square Root

# print(math.pow(2,3)) #Power

# print(math.floor(7.8))
# print(math.ceil(7.8))
# print(math.fabs(-5))

import random
# dice = random.randint(1,10)
# print(dice)

# student=["Rahul","karan","vishal","Neha"]
# selected=random.choice(student)
# print("Congratulation:",selected)

# r=random.randint(1000,9999)
# print (r)

import datetime
# current = datetime.datetime.now()
# print(current)

# Today = datetime.date.today()
# current.date
# current.month
# current.year

# date1=datetime.date(2026,1,1)
# date2=datetime.date(2026,1,29)
# diff = date2-date1
# print(diff)

# from collections import Counter

# fruits=["banana","Apple","Pineapple","Mango","banana","Apple","Pineapple","Mango","banana","Apple","Pineapple","Mango"]
# count=Counter(fruits)
# print(count)


# sentence = "Python is easy and python is powerful"
# a=sentence.split()
# print(a)



import os
# current_path = os.getcwd()
# print("current.path:",current_path)

# a=input("Enter the command:")

# item = os.listdir()
# print("items:",item)
# if a == "ls":
#     print(item)
# else:
#     print("Invalid Command")

import os

Folder_name = "My_Folder"

if not os.path.exists(Folder_name):
    os.mkdir(Folder_name)
    print("Folder Created Successfully")
else:
    print("Folder is already present")


