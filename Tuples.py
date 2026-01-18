tup = (1, 2, 3, 4, 5)
print(type(tup))
print(tup[0])
print(tup[3])
tup = () #empty tuple (valid)
print(tup)
tup = (1,) #for single element tuple, always enter a comma after the element (must)
tup = (1) #otherwise it will return the type of element present, instead of tuple
print(tup)

tup1 = (1, 2, 3, 4, 5, 3)
print(tup1[1:4]) #Tuples slicing

print(tup1.index(3)) #returns index of the element first occurrence
print(tup1.count(3)) #counts total occurrences

Grade = ("C","D","A","A","B","B","A","B","A","A","C","C","D","D","C","C","C","D","B","B","A","C")
grade = Grade.count("A")
print(grade)
print(Grade.count("B"))
print(Grade.count("C"))
print(Grade.count("D"))