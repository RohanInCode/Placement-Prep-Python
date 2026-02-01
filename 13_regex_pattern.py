import re
#1

# text="cat cot c@t"
# result=re.findall("c.t",text)
# print(result)

#2
# text="Hello World"
# print(bool(re.search("^Hello",text)))
# print(bool(re.search("^World",text)))

#3
# print(bool(re.search("Hello$",text)))
# print(bool(re.search("World$",text)))


#4
#0 or more (*)

# text ="helloooo"
# result = re.findall("lo+",text)
# print(result)

# text="color clolur"
# result=re.findall("colou?r",text)
# print(result)

# #7.Character set([])
# text = "apple ball cat"
# result=re.findall("[abv]",text)
# print(result)

# #8.Digits([0-9])
# text="My age is  30"
# result=re.findall("[0-9]",text)
# print(result)

#9
# text = "MY AGe is 40"
# result=re.findall("[A-Z]",text)
# print(result)

# 10
# text = "you are greAT AT codING"
# result=re.findall("[a-z]",text)
# print(result)

#11 All cap and small characters
# text="You are GREAT at Coding"
# result=re.findall("[A-z a-z]",text)
# print(result)

#12 Digits
# text = "MY 78e is 40"
# result=re.findall("[\d]",text)
# print(result)

#13 Non Digits
# text="My age is 21 and 2005"
# result=re.findall("[\D]",text)
# print(result)

#14 Word Character
# text="Marks: 90"
# result=re.findall("[\w]",text)
# print(result)

#15 No Char
# text = "Marks: 90"
# result=re.findall("\W",text)
# print(result)

# 16 Space 
# text="Ma rks: 90"
# result=re.findall("\s",text)
# print(result)

#17 No space
# text="Marks: 90"
# result=re.findall("\S",text)
# print(result)

#18
# text="Phone: 7993141314"
# results=re.findall("\d{10}",text)
# print(results)

#19 OR Opereator
# text="I have a cat and a dog"
# results=re.findall("Cat|Dog",text)
# print(results)

#20 Grouping
text= "abab ab"
results=re.findall("(ab)+",text)
print(results)
