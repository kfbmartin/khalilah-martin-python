#Khalilah Martin

#Section 1: Variables and Types
name = "Khalilah"
age = 49
height = 5.6
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2: User Input and Math
name = input('What is your name? ')
birth_year = int(input('What year were you born? '))

print (f"Hi, {name}! You are approximately {2026-birth_year} years old.")

num1 = float(input('Please enter a number:'))
num2 = float(input('Please enter a another number:'))

#Section 3: Type Conversion and f-strings
print(f"The numbers you entered is {num1} and {num2}.")  
print(f"{num1} x {num2} is {num1*num2}.")

#Section 4: Formatted Receipt
print("==========================")
print("           RECEIPT")
print("==========================")

item = 'T-Shirt'
price = 19.99
quantity = 1
print(f"Item: {item}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")

print("--------------------------")
print(f"Total: ${quantity*price}")
print("==========================")

#Section 5: Mini-Project - Profile Card
username = input('What is your name? ')
hometown = input('What is your hometown? ')
hobby = input('What is your favorite hobby? ')
fact = input('What is one fun fact about yourself? ')
birthYear = int(input('What year was you born? '))

print("")
print("╔══════════════════════════════╗")
print(f"           PROFILE: {username}")
print("╚══════════════════════════════╝")
print(f"Hometown: {hometown}")
print(f"Hobby:    {hobby}")
print(f"Fun fact: {fact}")
print(f"Age:      {2026-birthYear}")
