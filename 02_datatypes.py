 # =========================================================
# 🔹 DATA TYPES
# =========================================================


a = "Rohan"
print(type(a))
print(2 * a)



# =========================================================
# 🔹 TYPE CONVERSION
# =========================================================


salary = "50000"
a = int(salary)
print(a + 5000)



# =========================================================
# 🔹 LISTS
# =========================================================


marks = [10,80,30,40]
print(marks[2])
marks.append(100)
print(marks)
marks.insert(2,70)
print(marks)
a = len(marks)
print(a)
marks.remove(70)
print(marks)
marks.sort()
print(marks)


# Two sum (two pointer)   
target = 9
nums=[2,3,5,7]
left = 0
right= len(nums)-1
while left<right:
    current_sum = nums[left]+nums[right]
    if current_sum== target:
       print(nums[left],nums[right])
       break
    elif current_sum<target:
       left+=1
    else:
       right-=1


# Slow fast pointer example
nums = [10,20,30,40,50]
slow = 0
fast = 0
while fast<len(nums) and fast+1<len(nums):
   slow+=1
   fast+=2
print(nums[slow])




# Simple question bank

que = ["print(Hello world)" ,"print(6/3)"]
ans = ["Hello World" , "2"]
for i in que:
    print(i)

    

# =========================================================
# 🔹 TUPLES
# =========================================================


days = ('monday','tuesday','wednesday','thursday')
print(days)
print(days.count('monday'))
print(days.index('tuesday'))
print(len(days))



# =========================================================
# 🔹 SETS
# =========================================================


numbers= {10,20,30,40}
print (numbers)
numbers.add(100)
print (numbers)
numbers.update([120,130])
print (numbers)
numbers.remove(120)
print (numbers)
numbers.discard(140)
print (numbers)
numbers.pop()
print (numbers)



# =========================================================
# 🔹 DICTIONARY
# =========================================================


Student = { "name" : "rohan", "age" : 2 , "city" : "Delhi" , "course" : "python"}

print (Student)
print(Student["name"])
print(Student.get("age"))
print(Student.keys())
print(Student.values())





# =====================================================
# 🔹 LIST / TUPLE / SET / CONVERSIONS
# =====================================================

# Creating list and printing
'''
marks = [10, 20, 30, 40, 50]
print(marks)

for i in marks:
    print(i)
'''

# Append
'''
marks.append(90)
print(marks)
'''

# Sum
'''
print(sum(marks))
'''

# Sum using loop
'''
total = 0
for i in marks:
    total += i
print(total)
'''

# Reverse list
'''
nums = [10, 12, 34, 54]
print(nums[::-1])
'''

# Remove duplicates
'''

nums = [1,2,2,3,4,4,5,5]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)
'''


# List → Tuple
'''

numbers_tuple = tuple(nums)
print(numbers_tuple)
'''


# Tuple → List
'''

color = ("red","blue","green")
color_list = list(color)
print(color_list)
'''


# List → Set
'''

num_set = set(nums)
print(num_set)
'''


# Set → Dictionary
'''

subjects = {"Maths","Science","English"}
subject_dict = dict.fromkeys(subjects,100)
print(subject_dict)
'''