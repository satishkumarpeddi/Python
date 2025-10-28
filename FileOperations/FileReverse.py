file_name = input("Enter the file name  (with extension): ")
try:
    with open(file_name,'r') as file:
        print("\nReversed lines:\n")
        for line in file:
            print(line.strip()[::-1])
except FileNotFoundError:
    print("File not found.")
