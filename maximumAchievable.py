def max_product_method(numbers):
    max_product = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            product = numbers[i]*numbers[j]
            if product>=max_product:
                max_product = product 
    return max_product
numbers = list(map(int,input("Enter values : ").split()))
maxProduct = max_product_method(numbers)
print("Result : ",maxProduct)