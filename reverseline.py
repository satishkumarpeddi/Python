input = "input.txt"
# output = "output.txt"
try:
    with open(input,'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line[::-1])
except FileNotFoundError:
    print("Error: File Not Found Exception")
    