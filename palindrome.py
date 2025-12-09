def isPalindrome(num):
    return str(num)==str(num)[::-1]
def maxMinPalindrome(numbers):
    palindrome = list(num for num in numbers if isPalindrome(num))
    print(max(palindrome))
    print(min(palindrome))
numbers = list(map(int,input("Enter value : ").split()))
maxMinPalindrome(numbers)