def add(list,element):
    list.append(element)
def insert(list,element,i):
    if 0<=i<=len(list):
        list.insert(i,element)
def slices(list,start,end):
    if 0<=start<=end<=len(list):
       return list[start:end]
my_list = [10, 20, 30, 40, 50]

# Addition
add(my_list, 60)
print("After addition:", my_list)

# Insertion
insert(my_list, 25, 2)
print("After insertion:", my_list)

# Slicing
result = slices(my_list, 1, 4)
print("Sliced list:", result)