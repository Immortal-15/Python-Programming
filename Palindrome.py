#check if a list is palindrome or not

list = [1,2,3,2,1]
# list = [1,2,3,4,5]
# list = ["a","b","c","b","a"]
# list = ["a","b","c","d","e"]
# list = [1,"a",2,"b",3,"b",2,"a",1]

newlist = list.copy()
newlist.reverse()

if(newlist == list):
    print("The list is a Palindrome list")
else:
    print("The list is not a Palindrome list")