n = int(input("Enter number of items in dictionary : "))
dictionary = {}
for i in range(n):
    key = input().strip()
    value = int(input())
    dictionary[key]=value
print(sum(dictionary.values()))