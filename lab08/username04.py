first = input("Enter your first name : ")
last = input("Enter your last name : ")
gender = input("Enter your gender: ")

username = (gender + last[0] + first).upper()

print(username)