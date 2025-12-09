a = float(input("Enter value for a : "))
b = float(input("Enter value for b : "))
c = float(input("Enter value for c : "))
# if a>=b and a>=c:
#     print(a)
# elif b>=c:
#     print(b)
# else:
#     print(c)
# print(max(a,b,c))
result = a if a>=b else b
print(result)
