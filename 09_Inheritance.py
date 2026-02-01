# class Human:
#      def eat(self):
#          print("Human can eat")
    

# class Student(Human):
#      def study(self):
#         print("Students can study")

# s1= Student()
# s1.study()
# s1.eat()


# class Animals:
#     def speak(self):
#         print("Animals can speak")
# class Dogs(Animals):
#     def bark(self):
#         print("Dogs can only bark")
        
# a1= Dogs()
# a1.bark()
# a1.speak()


# class Nokia:
#     def pc(self):
#         print("Nokia can only call")
# class Iphone(Nokia):
#     def ctrl(self):
#         print("Ip can call and access the internet")

# p1=Iphone()
# p1.pc()
# p1.ctrl()


# class Parent:
#     def __init__(self):
#         print("This is a parent class")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("this is child constructor")

# obj=Child()


# class Parent:
#     def work(self):
#         print("I will go to work")
# class Child(Parent):
#     def work(self):
#         print("I will go to school")

# obj=Child()
# obj.work()



# class Parent:
#     def oc(self):
#         print("I am a Software Dev")
# class Mother:
#     def work(self):
#         print("I am a house wife")
    
# class Child(Parent,Mother):
#     def __init__(self):
#         print("I go to school")

# obj=Child()
# obj.oc()
# obj.work()



# class Parent:
#     def shape(self):
#         print("Square")
# class Child(Parent):
#     def shape(self):
#         print("Circle")
#         super().shape()

# obj = Child()
# obj.shape()



# class Teacher:
#     def teach(self):
#         print("Teacher is Teaching")
# class Coder:
#     def code(self):
#         print("Coder codes")
# class Student(Teacher,Coder):
#     # def __init__(self):
#     #     print("Student studies and pass the exam")
#     pass

# obj=Student()
# obj.code()
# obj.teach()




# class Parent:
#     def __init__(self):
#         self.__x=10

# class Child(Parent):
#     def show(self):
    
#         print(self.__x)
# obj=Child()
# obj.show()



# class Parent:
#     def __init__(self):
#         self.__x=10

# class Child(Parent):
#     def show(self):
#         print(self._Parent__x)


# obj=Child()
# obj.show()



# class Parent:
#     def __init__(self):
#         self._x=100
# class Child(Parent):
#     def show(self):
#         print(self._x)

# # obj=Child()
# # obj.show()

# obj1=Parent()
# print(obj1._x)




#QUESTION

class Person:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
class Student(Person):
    def show_name(self):
        print("My name is",self.get_name())

s1=Student("Rohan")
s1.show_name()

