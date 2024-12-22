import string
def check(password):
    if len(password)<8 or len(password)>15:
        print("Weak: Password should follow the range")
    if not any(char.islower() for char in password):
        print("Weak: Password should have lower case letter")
    if not any(char.isupper() for char in password):
        print("Weak: Password should have a  uppercase letter")
    if not any(char.isdigit() for char in password):
        print("Weak: Password should have a digit")
    if not any(char in string.punctuation for char in password):
        print("Weak: Use special character")
    if " " in password:
        print("Weak: Should not contain any whitespaces")
    if password.endswith(('.','@')):
        print("Weak: Should not end with . or @")
    else:
        print("Strong password")

password=input("Enter you password: ")
check(password)
