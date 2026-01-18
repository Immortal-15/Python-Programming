x = 1
while x <= 5 : #printing the string
    print("Hello World")
    x += 1

i = 1
while i <= 10 : #printing the number (straight order)
    print (i)
    i += 1

j = 5
while j >= 1 : #(reverse order)
    print(j)
    j -= 1

k = 1
while k<= 100 : #from 1 to 100
    print(k)
    k += 1

l = 100
while l >= 1 : #from 100 to 1
    print(l)
    l -= 1

n = int(input("Enter a number: ")) #table of the input number
o = 0
while o <= 10 :
    print(n * o)
    o += 1

a = 1
while a <= 10 :
    print(a*a)
    a += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #list
idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) #tuple
b = int(input("Enter a number: ")) #must be between (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
c = 0
while c < len(tup) :
    if(tup[c] == b):
        print("Found at idx", c)
    c += 1

d = 1
while d <= 5:
    print(d)
    if (d == 3):
        break    #break (keyword) function is used to terminate the loop when encountered
    d += 1

e = 0
while e <= 5:
    if (e == 3):
        e += 1
        continue    #continue skips the mentioned iteration and continues from the next iteration
    print(e)
    e += 1

f = 1
while f <= 10:
    if (f % 2 == 0):
        f += 1
        continue  #skips all even numbers and prints all odd numbers
    print (f)
    f += 1

f = 1
while f <= 10:
    if (f % 2 != 0):
        f += 1
        continue  #skips all odd numbers and prints all even numbers
    print (f)
    f += 1

list = [1, 2, 3, 4, 5]
for val in list:
    print(val)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for num in tup:
    print(num)
else:                  #for loop with else (optional)
    print("Completed")

str = "SubhojitDutta"
for char in str:
    if char == "t":
        print("Found :", char)
        break                   #when using break, if the main statement's work gets completed first, then the else statement won't execute
    print(char)
else:
    print("Completed")

for a in range(1, 11):
    print(a * a)
