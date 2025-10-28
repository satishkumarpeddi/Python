def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
lower = int(input("Enter lower limit of the range: "));
upper = int(input("Enter upper limit of the range: "));
print(f"Prime numbers between {lower} and {upper} are:");
for  number in range(lower,upper+1):
    if is_prime(number):
        print(number,end=" ")