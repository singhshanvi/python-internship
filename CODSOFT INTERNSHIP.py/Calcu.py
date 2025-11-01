num1 =float(input("Enter first number:"))
num2 =float(input("Enter second number:"))

print("select operation;")
print("+ for Addition")
print("-for substraction")
print("*for multiplication")
print("/for division")

choice = input("Enter your choice(+,-,*,/):")

if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*':
    result = num1 * num2
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print("Result:", result)
