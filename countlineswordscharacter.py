input = "input.txt"
# output = "output.txt"
try:
    with open(input,'r') as file:
        lines = file.readlines()
    num_lines=len(lines)
    num_words=sum(len(line.split()) for line in lines)
    num_char= sum(len(line) for line in lines)
    
    print(num_words,num_char,num_lines)
except FileNotFoundError:
    print("Error: File Not Found Exception")
    