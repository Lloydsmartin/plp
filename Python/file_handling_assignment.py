# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Line 3: Python File Handling\n")
except IOError as e:
    print("Error occurred while creating the file:", e)
else:
    print("File 'my_file.txt' created successfully.")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        file_contents = file.read()
        # Display the contents on the console
        print("Contents of 'my_file.txt':\n", file_contents)
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read the file.")
except IOError as e:
    print("Error occurred while reading the file:", e)

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Appending line 4.\n")
        file.write("67890\n")
        file.write("Line 6: File Handling in Python\n")
except IOError as e:
    print("Error occurred while appending to the file:", e)
else:
    print("Content appended to 'my_file.txt' successfully.")

# Error Handling using try, except, and finally blocks
try:
    # Try to open a non-existent file
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print("Error occurred:", e)
finally:
    print("This block always executes, regardless of exceptions.")
