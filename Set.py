collection = {1, 2, 3, 4, "Hello", "World"}
#collection = {1, 2, 2, 3, 3, 4, "Hello", "World", "World"} #Ignores any repetitions of elements
print(collection)
print(type(collection))
print(len(collection))

null_set = set()
print(type(null_set))
print(null_set)

null_set.add(1) #adds the element
null_set.add(2)
null_set.add(2) #ignores duplicate values
null_set.add("Hello")
null_set.add("World")
null_set.add((3,4,5))
null_set.remove(1) #removes the element
null_set.remove("World")
null_set.clear() #empties the set

print(null_set)
print(len(null_set))

pop_set = {"Hello", "World", "How", "Are", "You", "?"}
print(pop_set.pop()) #picks and prints a random element

set1 = {1, 2, 3, 5}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1) #no change as its unique
print(set2) #no change as its unique

print(set1.intersection(set2))


classroom = {
    "Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"
}
print(classroom)
print(len(classroom))

values = {
    9, "9.0", "9", #different ways to store same values in a set
    ("float", 9.0),
    ("int", 9),
}
print(values)