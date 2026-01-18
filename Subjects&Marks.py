marks = {}

x = int(input("Physics marks : "))
marks.update({"Physics" : x})
y = int(input("Chemistry marks : "))
marks.update({"Chemistry" : y})
z = int(input("Maths marks : "))
marks.update({"Maths" : z})
w = int(input("Computer marks : "))
marks.update({"Computer" : w})
p = int(input("English marks : "))
marks.update({"English" : p})

print(marks)
