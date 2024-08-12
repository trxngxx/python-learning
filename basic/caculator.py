print("Calculator Program")
first_number = input("first number: ")
second_number = input("second number: ")

print("The sum is", int(first_number) + int(second_number))
print("The division is", int(first_number) / int(second_number) if int(second_number) != 0 else "Error: Division by zero")
print("The multiplication is", int(first_number) * int(second_number))
print("The subtraction is", int(first_number) - int(second_number))
