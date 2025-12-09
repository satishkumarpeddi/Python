keys = input().split()
values = input().split()
if len(keys)!=len(values):
    print("Not valid")
else:
    my_dict = dict(zip(keys,values))
    new_key,new_value = input().split()
    print(my_dict)
    # totalvalue=sum(my_dict.values())
    print(dict(sorted(my_dict.items())))