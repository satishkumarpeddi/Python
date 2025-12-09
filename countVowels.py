def vowelsMethod(string):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in string if ch in vowels)
string = input("Enter string : ")
count = vowelsMethod(string)
print(count)