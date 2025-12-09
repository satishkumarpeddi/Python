def squareOddMethod(numbers):
    result = []
    for num in numbers:
        if num%2!=0:
            result.append(num**2)
    return result
            
numbers = list(map(int,input("Enter value : ").split()))
result = squareOddMethod(numbers)
print(result)