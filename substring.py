def findMethod(string,substring):
    count =0
    i =0
    while i<=len(string):
        if string[i:i+len(substring)]==substring:
            count+=1
        i+=1
    return count
string = input("Enter a string : ")
substring = input("Enter a substring : ")
occurance  = findMethod(string,substring)
print(occurance)