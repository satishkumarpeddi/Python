keys = input().split()
values = input().split()
if len(keys)!=len(values):
    print("Not valid")
else:
    my_dict = dict(zip(keys,values))
    new_key,new_value = input().split()
    print(my_dict)
    my_dict[new_key]=new_value
    print(my_dict)