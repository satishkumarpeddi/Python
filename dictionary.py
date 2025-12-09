keys = input().split()
values = input().split()
if len(keys)!=len(values):
    print("Not valid")
else:
    my_dict = dict(zip(keys,values))
    search = input().strip()
    if search in my_dict:
        print("Found")
    else:
        print("Not found")