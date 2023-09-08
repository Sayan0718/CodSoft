
import random
import string

print("""
    HELLO USER
WELCOME TO RANDOM PASSWORD GENERATOR""")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special_symbols = string.punctuation

combination = lower + upper + digits + special_symbols

l = int(input("Enter The Length Of The Password = "))

temp = random.sample(combination, l)

password = "".join(temp)

print("You Password Of ",l, " Size Is Created")
print("Password = ", password)

print("THANK YOU FOR USING")

