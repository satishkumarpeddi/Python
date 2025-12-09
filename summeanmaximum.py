def method(numbers):
    """
    Docstring for method
    
    :param numbers: Description
    """
    sumValue = sum(numbers)
    mean = sumValue/len(numbers)
    maxValue = max(numbers)
    return sumValue,mean,maxValue
numbers = list(map(int,input("Enter values : ").split()))
sumValue,mean,maxValue=method(numbers)
print(sumValue,mean,maxValue)