"""import random
import string
chars = string.ascii_letters + string.digits + string.punctuation

pass_length = int(input("Enter the desired password length: "))
password = ""
for i in range(pass_length):
    password += random.choice(chars)
print(f"Your password is: {password}")"""

import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation
pass_length = int(input("Enter the desired password length: "))

password = ""
for i in range(pass_length):
    password += secrets.choice(chars)
#password = "".join(secrets.choice(chars) for _ in range(pass_length))      #another way to run the loop known as list comprehension.
print(f"Your password is: {password}")
