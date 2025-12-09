def add_element(listVisual,element):
    listVisual.append(element)
    print("Element add successfully.")
def insert(listVisual,element,index):
    if 0<=index<=len(listVisual):
        listVisual.insert(index,element)
        print("Element is insert at particular position")
def slicing(listVisual,start,end):
    if 0<=start<=end<=len(listVisual):
        new_list = listVisual[start:end]
        print("After slicing : ",new_list)
        
listVisual = []
while True:
    print("1. Add to list :")
    print("2. Insert into the list : ")
    print("3. Slicing the list : ") 
    operation = input("Enter required operation : ")
    if operation == '1':
        element = int(input("Enter a element to add to list : "))
        add_element(listVisual,element)
    elif operation == '2':
        element = int(input("Enter a element to add to list : "))
        index = int(input("Enter a index to insert : "))
        insert(listVisual,element,index)
    elif operation == '3':
        start = int(input("Enter starting index : "))
        end = int(input("Enter ending index : "))
        slicing(listVisual,start,end)
    else:
        break
print(listVisual)