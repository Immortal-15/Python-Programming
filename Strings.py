#Three different valid strings with different quotes sign
# str1 = "This is a string" #Mostly used way to write a string
# str2 = 'This is a string'
# str3 = """This is a string"""
#str4 = " " #Valid to print a blank string anywhere (maybe use to give a space in between strings)
# str4 = "This is a string. \nIt is created in python." #(next line)
# str5 = "This is a string. \tIt is created in python." #(tab)
# print(str4)
# print(str5)

#Concatenation
"""str1 = "Python"
str2 = "String"
final_str = str1 + " " + str2
print(final_str)"""

#String Length
"""str1 = "Python String"
len1 = len(str1)
print(len1)"""

#Indexing
"""str = "Python String"
ch = str[0]
print(ch)
print(str[3]) """

#Slicing
"""str = "Python String"
print(str[1 : 6]) #+ve index
print(str[ : 8])
print(str[0 : 8])
print(str[2 : ])
print(str[2 : len(str)])

print(str[-10 : -2]) #-ve index
print(str[ : -2])
print(str[-10 : ])"""

#String Functions
"""str = "this is a Python String."

print(str.endswith("ing.")) #returns true if the given string ends with the mentioned substring
print(str.capitalize()) #capitalizes the first letter, doesn't change the original string, only changes when the function is called
print(str.replace("Python", "Java")) #replaces all current occurrences of old with new
print(str.find("Python")) #returns the first index of the first occurrence
print(str.count("is")) #counts the occurrence of the mentioned substring in the given string"""

"""greet = "Hello World!"
low = greet.lower()     #changes every letter in the variable into small case letters
up = greet.upper()      #changes every letter in the variable into upper case letters
print(low)
print(up)

print("Hi There".lower())
print("Hi There".upper())
"""

"""greet = "          Hello Bob       "
print(greet.lstrip())      #removes left whitespaces
print(greet.rstrip())      #removes right whitespaces
print(greet.strip())       #removes both beginning and ending (left and right - both sides) whitespaces

line = "Have a nice day!"
print(line.startswith("Have"))      #searches for prefixes, if found returns true, else returns false
print(line.startswith("H"))
print(line.startswith("h"))     #startswith() function is case sensitive, so this statement returns false"""

"""str = ("Hello World! Welcome To Python")
print(str.split())      #Breaks the string in to individual words respective to the whitespaces (when a delimiter is not specified) and puts them all in a List

str = ("Hello;World!;Welcome;To;Python")
print(str.split(";"))       After using the delimiter for split function, it splits the string based on that delimiter (like ";" in this case)"""

#WAP to input user's first name and print its length
"""name = input("Enter your first name: ")
print("The length of the your name is: ", len(name))"""

#WAP to find the occurrences of '$' in a string
"""str = input("Enter a valid string: ")
print(str.count("$"))"""