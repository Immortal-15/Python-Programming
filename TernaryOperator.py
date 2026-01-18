#Single Line if

food = input ("Enter food name: ")
eat = "Yes" if food == "Cake" else "No"
print (eat)

print ("Sweet") if food == "Cake" or food == "Jalebi" else print ("Not Sweet")

#Clever if

age = int (input ("Enter your age: "))
vote = ("Yes" , "No") [age < 18]
print (vote)

sal = float(input("Enter your salary: "))
tax = sal*(0.1, 0.2) [sal>50000]
print (tax)