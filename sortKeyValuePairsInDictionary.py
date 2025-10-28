my_dict={
    'banana':3,
    'apple':5,
    'cherry':2,
    'mango':4
}
sorted_by_keys = dict(sorted(my_dict.items()))
sorted_by_values = dict(sorted(my_dict.items(),key=lambda item:item[1]))
print("Original Dictionary:",my_dict)
print("Sorted by Keys:",sorted_by_keys)
print("Sorted by Values:",sorted_by_values)