marks = [95.5, 85.5, 75.5, 65.5, 55.5] #list with multiple values separated by commas, and inputted within []
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[-1])

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of integers
numbers = [1, 5, 9, 20]

# A list with mixed data types
mixed_list = [10, "hello", True, 3.14]

#List is mutable
student = ["Subhojit", 19, "Barasat"]
student[-1] = "America"
student[1] = 20
print(student)

#List slicing
marks2 = [50, 60, 70, 80, 90, 100]
print(marks2[0:4])
print(marks2[1:6])
print(marks2[1:6:2])
print(marks2[:5])
print(marks2[1:])
print(marks2[-6:-3]) #negative index(starts from right side from -1)
marks2.append(110) #adds the given element at the end of the list
print(marks2)

list = [2, 4, 1, 5, 12, 10, 100, 55, 25, 75, 200, 500]
list.sort() #sorts the list in ascending order
print(list)
list.sort(reverse=True) #sorts the list in descending order
print(list)
list.reverse() #reverses the list
print(list)
list.insert(5, 200) #insert element at index
print(list)
list.remove(200) #removes first occurrence of the element
print(list)
list.pop(2) #removes element at index
print(list)

Grade = ["C","D","A","A","B","B","A","B","A","B","A","C","C","D","D","C","C","C","D","B","B","A"]
Grade.sort()
print(Grade)
