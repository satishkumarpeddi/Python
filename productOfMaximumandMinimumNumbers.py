numbers = list(map(int,input("Enter numbers separated by space: ").split()))
maximum = max(numbers)
minimum = min(numbers)
product = maximum*minimum
print("Maximum number: ",maximum)
print("Minimum number:",minimum)
print("Product of maximum and minimum numbers:",product)