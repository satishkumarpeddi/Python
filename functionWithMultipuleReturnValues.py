def calculate(a,b):
    addition = a+b
    substraction = a-b
    multiplication = a*b
    division = a/b
    return addition,substraction,multiplication,division
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add,sub,mul,div =calculate(num1,num2)
print("Addition : ",add)
print("Substraction : ",sub)
print("Multiplication : ",mul)
print("Division : ",div)