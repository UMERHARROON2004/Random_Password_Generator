import random
import string
password_length = 8         #we can set password length as we need
Char_val = string.ascii_letters + string.digits + string.punctuation      #we ca also use only 1 or 2 or 3 string it depend on us
password =""
for i in range(password_length):
    password += random.choice(Char_val)
print("Your randomly generated password is:\n",password)

