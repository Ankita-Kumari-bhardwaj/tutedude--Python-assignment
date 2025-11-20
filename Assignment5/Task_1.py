# defining dictionary
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diksha": 88,
    "Rahul": 76
}

# Asking the user to input student's name
name = input("Enter the student's name: ")

# checking if the student name is in the list or not
if name in students:
    # retrieving and displaying the corresponding marks
    print(f"{name}'s marks: {students[name]}")
else:
    # displaying a message when student's name is not found
    print("Student not found")
