"""name = "Subhojit Dutta"
age = 20
hobby = "Space Study"
print(name, age, hobby)
print("My name is: ", name)
print("My age is: ", age)
print("I love to do: ", hobby)"""

"""name = input("Enter your name = ")
age = int(input("Enter your age = "))
marks = float(input("Enter your marks = "))
print("My name is: ",name, "and my age is: ",age, "I got: ",marks, "in my b.tech course.")
print(type(name))
print(type(age))
print(type(marks))"""

"""light = input("Enter the traffic light: ")
if light.lower() == "red":
    print("Stop")
elif light.lower() == "yellow":
    print("Ready")
elif light.lower() == "green":
    print("Go")
else:
    print("Light is broken.")"""

"""num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("The sum is:", num1 + num2)"""

"""side1 = int(input("Enter the length of rectangle: "))
side2 = int(input("Enter the breadth of rectangle: "))
print("The area of the rectangle is:", side1 * side2)"""

"""side = int(input("Enter side of square :"))
print("The area of square is: ", side * side)
print("The area of square is: ", side ** 2)"""

"""num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print("The average is:", (num1 + num2) / 2)"""

"""a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if a >= b:
    print("True")
else:
    print("False")

print(a >= b) #another way to write it """

"""str1 = "Subhojit"
str2 = "Dutta"
concatenate = str1 + str2
print(concatenate)
print(len(concatenate))"""

"""str = "i am Subhojit Dutta"

print(str.endswith("tta"))
print(str.count("t"))
print(str.capitalize()) #doesn't change the original string. if needed then have to save this function in variable, example - str = str.capitalize()
print(str.replace("Subhojit", "Sayani"))
print(str.find("Subhojit"))
print(str.count("am"))"""

"""name = input("Enter your first name: ")
print(len(name))"""

"""str = input("Enter a string with multiple $: ")
print(str.count("$"))"""

"""marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Fail")"""

"""age = int(input("Enter your age: "))
if age >= 18:
    if age >= 70:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")"""

"""num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")"""

"""num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2:
    if num1 > num3:
        print("Greatest number is: ",num1)
if num2 > num3:
    if num2 > num1:
        print("Greatest number is: ",num2)
if num3 > num2:
    if num3 > num1:
        print("Greatest number is: ",num3)
else:
    print("invalid number")"""

"""num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Not divisible by 7")"""

#lists - mutable
"""marks = [99.9, 89.8, 79.7, 69.6, 59.5]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])

student = ["Subhojit", 99.9, "Barasat", 20]
print(student)
student[0] = "Sayani"
student[3] = 23
print(student)"""

"""marks = [99.9, 89.8, 79.7, 69.6, 59.5]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])"""

"""list = [2, 4, 1, 3]
list.append(5)
print(list)
list.sort()  #ascending
print(list)
list.sort(reverse=True)  #descending
print(list)
list.reverse()  #total list reverse
print(list)
list.insert(2, 6)
print(list)
list.remove(6)  #removes the given element's first occurence
print(list)
list.pop(2)  #removes element at given element
print(list)"""

#tuples - immutable
"""null_tup = () #valid
print(type(null_tup))
single_val_tuple = (1,)  #must have a comma after the element to be valid tuple
print(type(single_val_tuple))
tup = (1, 2, 3, 4, 5, 2, 2, 3, 2)
print(type(tup))
print(tup[1:4])
print(tup.index(4))  #index of first occurrences
print(tup.count(2))  #index of no of occurrences"""

"""m1 = input("Enter movie name: ")
m2 = input("Enter 2nd movie name: ")
m3 = input("Enter 3rd movie name: ")
list = [m1, m2, m3]
print("Your favourite movies are: ", list)

num = [1, 2, 3, 2, 1]
rev = num.copy()
rev.reverse()
if rev == num:
    print("Its a Palindrome list")
else:
    print("Not a Palindrome list")

ran = [1, "abc", "abc", 1]
rev1 = ran.copy()
rev1.reverse()
if rev1 == ran:
    print("Its a Palindrome list")
else:
    print("Not a Palindrome list")"""

"""grade = ("C", "D", "A", "A", "B", "B", "A")
print("Number of students with grade 'A' are: ", grade.count("A"))

grade1 = ["C", "D", "A", "A", "B", "B", "A"]
grade1.sort()
print(grade1)"""

#Dictionary - mutable
"""info = {
    "name" : "Subhojit", #string
    "age" : 20, #integer
    "subjects" : ("Python", "Java", "C", "C++", "DSA"), #tuple
    "marks" : [99.9, 99.8, 99.7, 99.6, 99.5], #list
    "grade" : 9.5, #float
    "is_adult" : True, #boolean
}
print(type(info))
print(info)
print(info["name"])
print(info["age"])
print(info["grade"])
print(info["marks"])
info["name"] = "Sayani"
info["age"] = 23
info["grade"] = 9.8
info["surname"] = "Dutta"
print(info)

null_dict = {}
print(null_dict)"""

"""student = {
    "name" : "Subhojit",
    "age" : 20,
    "subjects" : {          #nested dictionary
        "Python" : 99.9,
        "Java" : 99.8,
        "C" : 99.7,
        "C++" : 99.6,
        "DSA" : 99.5,
    },
    "grade" : 9.5,
}
print(student)
print(student["subjects"])
print(student["subjects"] ["Python"])
print(list(student.keys()))  #type casting to list and tuples
print(tuple(student.values()))
print(student.items())
print(student.get("subjects")) #returns value same as dict["key"] does, but during invalid key name, it returns none instead of error.
student.update({"city": "Barasat"})
print(student)"""

#Sets - mutable but its elements are immutable
"""nums = {1, 2, 3, 4, 5, 5, 4, 3, 4, 5, "hello", "world", 9.9, 9.8, 9.7}   #duplicate values gets deleted
print(type(nums))
print(len(nums))
print(nums)
null_set = set()
print(type(null_set))
null_set.add("hello")
null_set.add("world")
null_set.add("grade")
null_set.add(9.5)
print(null_set)
null_set.remove("world")
print(null_set)
null_set.pop()  #removes random value
print(null_set)
null_set.clear() #clears the whole set

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)     #returns a new set after combining sets
print(set3)

set4 = {1, 2, 3, 4, 5}
set5 = {3, 4, 5, 6, 7}
print(set4.intersection(set5))  #returns the common values in form of set after combining sets"""

"""meaning = {
    "table" : ["a piece of furniture" , "list of facts & figures"],
    "cat" : "a small animal"
}
print(type(meaning))
print(meaning)

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("No of classes needed for each subject are: ", len(subjects))"""

"""marks = {}
s1 = input("Enter first subject: ")
s2 = input("Enter second subject: ")
s3 = input("Enter third subject: ")
m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

marks.update({s1:m1, s2:m2, s3:m3})
print("You obtained the following marks: ", marks)

num = {9, "9.0", #or
("float", 9.0),
("int", 9)
       }
print(num)"""

#while loop
"""i = 1
while i <= 10:
    print(i)
    i += 1

j = 10
while j >= 1:
    print(j)
    j -= 1

hundred = 1
while hundred <= 100:
    print(hundred)
    hundred += 1

rev_hundred = 100
while rev_hundred >= 1:
    print(rev_hundred)
    rev_hundred -= 1

m = int(input("Enter a number: "))
n = int(input("Multiply upto: "))
o = 1
while o <= n:
    print(m * o)
    o += 1

num = 1
while num <= 10:
    print(num * num)
    num += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l = 0
while l < (len(nums)):
    print(nums[l])
    l += 1

x = int(input("Enter the square of a number within 10: "))
squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) # Avoid using 'list' as a variable name
k = 0
while k < len(squares):
    if squares[k] == x:
        print(f"Found {x} at index {k}")
        break       #ends
    k += 1
else:
    print("Number not found in the tuple.")

i = 0
while i <= 10:
    if i == 5:
        i +=1
        continue        #skips
    print(i)
    i += 1

i = 0
while i <= 10:
    if i % 2 == 0:          #odd numbers only
        i +=1
        continue
    print(i)
    i += 1

i = 0
while i <= 10:
    if i % 2 != 0:          #even numbers only
        i +=1
        continue
    print(i)
    i += 1"""

#for loop
"""nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in nums:
    print(val)
else:
    print("Loop ended")

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list:
    print(i)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a square of a number between 1 to 10: "))
n = 0
for k in tup:
    if k == x:
        print(f"Found {x} at index {n}")
        break
    n += 1
else:
    print("Number not found in tuple")"""

#range (start (default 0), stop, step (default 1))
"""for i in range(10):     #range(stop)
    print(i)

for i in range(2, 10):      #range(start, stop)
    print(i)

for i in range(1, 10, 2):       #range(start, stop, step)
    print(i)

for i in range(2, 11, 2):       #even no only upto 10
    print(i)

for i in range(1, 10, 2):       #odd no only upto 10
    print(i)

for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)

n = int(input("Enter a number whose table you want: "))
m = int(input("Enter a number upto which multiple you want: "))
for i in range(1, m):
    print(i * n)"""

#pass statement
"""for i in range(10):
    pass            #null statement

if i <= 20:
    pass"""

"""n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
sum = 0         #sum of n natural numbers upto m
while n <= m:
    sum += n
    n += 1
print("Total sum: ", sum)

f = int(input("Enter a number: "))
fact = 1
for a in range(1, f+1):
    fact *= a
print("Total factorial is: ", fact)"""

#Functions definition
"""def calc_sum(a, b):     #a, b are parameters
    sum = a + b
    return sum
print(calc_sum(105510, 205520))     #function calls, arguments

def print_hello():
    print("Hello World")
print_hello()
output = print_hello()
print(output)       #wont return any output.

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print("The average is: ", avg)
    return avg
calc_avg(1, 2, 3)
calc_avg(99, 98, 97)

def len_list(l):
    print("Length of the given list is:", len(l))
    return len(l)
len_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def print_list(l):
    for i in l:
        print(i, end=" ")
    return l
print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print()

def print_fact(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)
    return fact
print_fact(10)

def calc_fact(n):
    facto = 1
    for i in range(1, n+1):
        facto *= i
    print(facto)
    return facto
calc_fact(5)

def convert_currency(usd, exchange_rate=92.0):
    result = usd * exchange_rate
    return result

amount_usd = 100
amount_inr = convert_currency(amount_usd)

print(f"${amount_usd} USD is equal to ₹{amount_inr:,.2f} INR")

def odd_even():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("Even")
    elif num % 2 != 0:
        print("Odd")
    else:
        print("Invalid Number")
odd_even()"""

#Recursion
"""def show(n):
    if n == 0:      #base case
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n-1)        #recurrence relation
print(fact(5))

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
print(sum_n(5))

def elements(list, idx = 0):
    if idx == len(list):
        return
    print(list[idx])
    elements(list, idx + 1)

elements([1, 2, 3, 4, 5])"""

#File I/O
"""with open("sample.txt", "w") as text_file:
    text_file.write("Hello! This is a sample text file.\n")
    text_file.write("Python File I/O is pretty straightforward.")

with open("sample.doc", "w") as doc_file:
    doc_file.write("This is a sample document file created via Python.\n")
    doc_file.write("To make a 'real' .docx, you'd usually use the 'python-docx' library.")"""

"""f = open("sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#with code for auto closing the file
with open("sample.txt", "r") as f:
    data = f.read(5)        #outputs only first 5 letters/elements
    print(data)

with open("sample.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)"""

"""# with open("sample.txt", "w") as f:      #overwrites everything in the file
#     f.write("Hello there! \nI am Subhojit.")

# with open("sample.txt", "a") as f:
#     f.write("\n'a' means Append meaning it adds the given text at the end of the existing file. \nIt doesn't overwrite or delete any pre-existing data from the file")

#with open("sample.txt", "r+") as f:        #"r+" means read + write    #pointer at start, no truncate
#      f.write("Heyaa")      #this "r+" overwrites the data in the file from the starting, taking the same space that the given data needs, rest stays the same.

# with open("sample.txt", "w+") as f:         #"w+" means write + read      #truncate
#     f.read()        #this command deletes every data in the file like write normally would do
#     f.write("Hello, I am Subhojit.")        #this "w+" overwrites the total data in the file, and writes data totally new.

# "a+" also known as read + append, is used to read the file from the last of the file data, and appends any given data at the end of the file data.      #pointer at end, no truncate"""

"""import os
os.remove("sample.doc")     #removes the given file."""

"""with open("practice.txt", "w") as f:
    f.write("Hi everyone. \nWe are learning file I/O. \nusing Java. \nI like programming in Java.")

def replace_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        new_data = data.replace("Java", "Python")
        print(new_data)
    with open("practice.txt", "w") as f:
        f.write(new_data)
replace_word()

with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Data found")
    else:
        print("Data not found")

def check_line():
    line_number = 1
    with open("practice.txt", "r") as f:
        for line in f:
            if "learning" in line:
                print(f"data found at line: {line_number}")
                return
            line_number += 1
    return -1
check_line()

with open("numbers.txt", "r") as f:
    numbers = f.read().replace(',', ' ').split()

    for n in numbers:
        num = int(n)
        print(f"{num} is {'Even' if num % 2 == 0 else 'Odd'} number")"""

#OOP - Object Oriented Programming
"""class Student:      #creating a class
    name = "Subhojit"
s1 = Student()      #creating object(instances)
print(s1.name)

class Car:
    color = ("Red")
    brand = ("Bugatti")
    passenger = 2
c1 = Car()
print("Color is",c1.color, "\nBrand is", c1.brand, "\nPassenger capacity is", c1.passenger)"""

#Constructor
"""class Student:
    college_name = "Swami Vivekananda University"       #class attribute - something that is same for all instances
    def __init__(self, name, marks):
        self.name = name        #instances attribute - something that is different for all instances
        self.marks = int(marks)         #instances attribute - something that is different for all instances
    def welcome(self):      #functions used in class are known as methods
        print("Welcome to Swami Vivekananda University,", self.name)
s1 = Student("Subhojit", 99)
print(s1.name, s1.marks, s1.college_name)
s1.welcome()
s2 = Student("Sayani", 98)
print(s2.name, s2.marks, s2.college_name)
s2.welcome()"""

"""class Student():
    def __init__(self, name, submarks):
        self.name = name
        self.marks = submarks
    def get_average(self):          #non-static methods (needs self parameter), its object level method
        avg = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s average is: {avg}")
s1 = Student("Subhojit", [99, 97, 98])
s1.get_average()

class Hello():
    @staticmethod           #static method (doesnt need self as parameter), its class level method
    def hello():
        print("Hello, World!")
Hello.hello()"""

#Abstraction :- Hiding the implementation details of a class and only showing the essential features to the user
#Encapsulation :- Wrapping data and functions into a single unit (object)
"""class Account():
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    def Debit(self, amount):
        self.balance -= amount
        print(f"{self.acc_no}'s debited amount is: {amount}")
    def Credit(self, amount):
        self.balance += amount
        print(f"{self.acc_no}'s credited amount is: {amount}")
    def Final(self):
        print(f"{self.acc_no}'s final balance is: {self.balance}")
        return self.balance

acc1 = Account(2005, 9999999)
acc1.Debit(10000)
acc1.Credit(5000)
acc1.Final()"""

#del in OOP
"""class Student():
    def __init__(self, name):
        self.name = name
s1 = Student("Subhojit")
s2 = Student("Sayani")
print(s1.name)      #gets executed
del(s1.name)
print(s2.name)
print(s1.name)      #doesnt execute as its deleted"""

#private attributes
"""class bank():
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass          #putting (__) two underscores before any attribute makes it private, which cannot be accessed after calling publicly, i.e, outside of class.
    def reset_pass(self):
        print(self.__acc_pass)
acc1 = bank(123, "abc")
acc2 = bank(456, "def")
acc3 = bank(789, "ghi")
acc4 = bank(101, "jkl")
acc5 = bank(112, "mno")
print(acc1.reset_pass())        #this works as it's called inside class
print(acc1.__acc_pass)          #this won't work as it's called outside class"""

#Inheritance
#single inheritance
"""class Car:
    @staticmethod
    def start():
        print("Car started.")
    @staticmethod
    def stop():
        print("Car stopped.")
    @staticmethod
    def ready():
        print("Car ready to drive.")
class Bugatti(Car):
    def __init__(self, brand):
        self.brand = brand
#multi-level inheritance
class Chiron(Bugatti):
    def __init__(self, mileage, speed):
        self.mileage = mileage
        self.speed = speed
car1 = Chiron(50, 500)
print(car1.mileage)
print(car1.speed)
print(car1.start())"""

#Multiple Inheritance
"""class A:        #parent class
    varA = "Welcome to class A"
class B:        #parent class
    varB = "Welcome to class B"
class C(A, B):      #child class
    varC = "Welcome to class C"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)"""

#Super method
"""class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started.")
    @staticmethod
    def stop():
        print("Car stopped.")
    @staticmethod
    def ready():
        print("Car ready to drive.")
class Bugatti(Car):
    def __init__(self, name, type):
        self.brand = name
        super().__init__(type)
        super().start()
car1 = Bugatti("Chiron", "Diesel")
print(car1.type)"""

#class method decorator
"""class Person:
    name = "anonymous"
    # def change_name(self, name):
    #     self.name = name
    @classmethod        #used when needs changes at class level
    def change_name(cls, name):         #cls is the keyword like self, in place of self, used to indicate class method
        cls.name = name
p1 = Person()
p1.change_name("Subhojit")
print(p1.name)
print(Person.name)"""

#class method - (cls) base attribute
#instance method - (self) base attribute
#static method - no base attribute

#property decorator
"""class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    # def calcPercentage(self):
    #     self.percentage = str((self.maths + self.phy + self.chem) / 3) + "%"
    @property           #used when there is a chance of future changes to a/some attributes
    def percentage(self):
        return str((self.maths + self.phy + self.chem) / 3) + "%"
stu1 = Student(99, 98, 97)
print(stu1.percentage)
stu1.chem = 90
print(stu1.percentage)"""

#OOP 4 Pillars - Abstraction, Inheritance, Encapsulation, Polymorphism

#Polymorphism - when same operator is allowed to have different meanings
"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNum(self):
        print(self.real, "i +", self.img, "j")
    def __add__(self, num2):        #__add__ is dunder function, any operator can be overloaded using dunder functions
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
num1 = Complex(2,3)
num1.showNum()
num2 = Complex(3,4)
num2.showNum()
num3 = num1 + num2
num3.showNum()

#same can be done for __sub__, __mul__, __truediv__"""

"""import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def dia(self):
        return self.radius * 2
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(49)
print(f"Diameter: {c1.dia()}")
print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")"""

"""class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)
class Engineer(Employee):
    def __init__(self, name,  age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "1,00,000 INR")
    def showDetails(self):
        print("--- Employee Portal ---")
        print("Name =", self.name)
        print("Age =", self.age)
        super().showDetails()
eng1 = Engineer("Subhojit Dutta", 21)
eng1.showDetails()"""

"""class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, ordr2):
        return self.price > ordr2.price
ordr1 = Order("Chocolate", 100)
ordr2 = Order("Milk", 50)
print(ordr1 > ordr2)"""

#mostly used/required characters
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)