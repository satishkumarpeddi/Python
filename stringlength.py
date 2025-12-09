def lenMethod(string):
    count=0
    for ch in string:
        count+=1
    return count
string = input("Enter string : ")
length = lenMethod(string)
print(length)