# Task 2: Write, Append, and Read File

# Step 1: Write user input to output.txt
with open('output.txt', 'w') as fh:
    text1 = input("Enter text to write to the file: ")
    fh.write(text1 + "\n")
    print("Data successfully written to output.txt.")

# Step 2: Append more input to the same file
with open('output.txt', 'a') as fh:
    text2 = input("Enter additional text to append: ")
    fh.write(text2 + "\n")
    print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as fh:
    content = fh.read()
    print(content)
