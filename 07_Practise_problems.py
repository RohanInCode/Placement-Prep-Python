# =====================================================
# 🔹 PROBLEM SOLVING PROGRAMS
# =====================================================


# Move zeros to end
nums=[0,1,0,8,3,12]
results=[]
zero_count=0

for n in nums:
    if n==0:
        zero_count+=1
    else:
        results.append(n)

for _ in range(zero_count):
    results.append(0)

print(results)


# Palindrome check
text = "madam"

left=0
right=len(text)-1
isPalindrome=True

while left<right:
    if text[left]!=text[right]:
        isPalindrome=False
        break
    left+=1
    right-=1

print(isPalindrome)


# Longest word
sentence = "Python makes problem solving fun"
words = sentence.split()

longest=""
for i in words:
    if len(i)>=len(longest):
        longest=i

print(longest)


# Two sum (two pointer)
target = 9
nums=[2,3,5,7]

left=0
right=len(nums)-1

while left<right:
    current_sum = nums[left]+nums[right]

    if current_sum==target:
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
que = ["print(Hello world)", "print(6/3)"]
ans = ["Hello World", "2"]

for q in que:
    print(q)
