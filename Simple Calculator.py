print("\nRyan's Calculator\n")


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")
operation = int(input("Enter your op eration: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if operation == 1:
    print(num1, "+", num2, "=", num1+num2)

elif operation == 2:
    print(num1, "-", num2, "=", num1-num2)

elif operation == 3:
    print(num1, "*", num2, "=", num1*num2)

elif operation == 4:
      print(num1, "/", num2, '=', num1 / num2)