info = {
    "Name" : "Subhojit Dutta",
    "Age" : 20,
    "Marks" : [99, 98, 97, 96, 95],
    "Grade" : "A+",
    "CGPA" : 9.5,
    "is_adult" : True
}
print(info)
print(info["Name"])
print(info["Age"])
print(info["Marks"])
print(info["Grade"])
print(info["CGPA"])
print(info["is_adult"])

info["Name"] = "Subhojit" #can change key-values in dictionary as its mutable
info["Surname"] = "Dutta" #can add new key in dictionary as its mutable
print(info)

null_dict = {} #empty dictionary
print(null_dict)

#Nested dictionaries
student = {
    "Name" : "Subhojit Dutta",
    "Age" : 20,
    "Subjects" : {
        "Physics" : 99,
        "Chemistry" : 98,
        "Engineering" : 97,
        "Mathematics" : 96,
        "AI/ML" : 95,
    }
}

print(student)
print(student["Subjects"]) #for printing particular keys, values
print(student["Subjects"] ["Physics"])
print(len(student)) #OR
print(len(list(student.keys())))

#dictionaries methods
print(student.keys()) #returns all keys
print(list(student.keys())) #type casting to list
print(student.values()) #returns all values
print(list(student.values())) #type casting to list
print(student.items()) #returns all (key, val) pairs as tuples
print(list(student.items())) #type casting to list
print(student.get("Subjects")) #returns the key according to the value
student.update({"City" : "Kolkata"}) #inserts the specified items to the dictionary
student.update({"Country" : "India" , "District" : "North 24 Parganas"})
print(student)

meaning = {
    "Table" : ["A piece of furniture" , "list of facts and figures"],
    "Cat" : "a small animal"
}
print(meaning)