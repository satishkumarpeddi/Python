input = "input.txt"
output = "output.txt"
try:
    with open(input,'r') as file:
        lines = file.readlines()
    sorted_lines = sorted([line.strip() for line in lines])
    with open(output,'w') as file:
        for line in sorted_lines:
            file.write(line+"\n")
    print("Sorted lines : ")
    for line in sorted_lines:
        print(line)
except FileNotFoundError:
    print("Error: File Not Found Exception")
    