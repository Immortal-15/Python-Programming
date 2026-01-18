#Arithmetic operators

a = 15
b = 5

sum= (a + b)
deduct = b - a

print(sum)
print(deduct)
print(a + b) #add
print(a - b) #substract
print(a * b) #multiply
print(a / b) #divide
print(a % b) #remainder
print(a ** b) #a^b


#Relational Operators

x = 50
y = 100

print(x == y) #equal
print(x != y) #not equal
print(x > y) #greater than
print(x < y) #less than
print(x >= y) #greater than, equal
print(x <= y) #less than, equal


#Assignment Operators

num = 10 # Assigns value 10 to the variable 'num'.
num += 10 # Equivalent to num = num + 10. Adds 10 to 'num' and updates 'num'.
num -= 10 # Equivalent to num = num - 10. Subtracts 10 from 'num' and updates 'num'.
num *= 10 # Equivalent to num = num * 10. Multiplies 'num' by 10 and updates 'num'.
num /= 10 # Equivalent to num = num / 10. Divides 'num' by 10 and updates 'num'.
num %= 10 # Equivalent to num = num % 10. Calculates the remainder when 'num' is divided by 10 and updates 'num'.
num **= 10 # Equivalent to num = num ** 10. Raises 'num' to the power of 10 and updates 'num'.


#Logical Operators

e = 50
f = 100

print(not False)
print(not True)
print(not (e < f))

# Correct usage of 'and' and 'or' would involve two operands
print(True and False) # Example of 'and'
print(True or False)  # Example of 'or'
print((e < f) and (f > e)) # Example with variables
print((e < f) or (f < e))  # Example with variables
