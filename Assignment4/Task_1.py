# Task 1: Read a File and Handle Errors
# This program opens a file named 'sample.txt',
# prints its content line by line with line numbers,
# and handles the case where the file does not exist.

try:
    # Try to open the file in read mode
    with open("sample.txt", 'r') as file:

        # Display header before printing file content
        print("Reading file content:\n")

        line_number = 1  # To count and print line numbers

        # Read and print each line one by one
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

# If the file is missing, this block runs
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
