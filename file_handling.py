# Script Name:                    File Handling
# Author:                         Kevin Williams
# Date of Lastest revision:       12/8/2023
# Purpose:                        Open and manipulate an existing file 
# Additional Sources:             https://chat.openai.com/share/563dfa4e-7a05-4490-a19c-335228728dbc

# Create a new text file
file_path = 'example.txt'
with open(file_path, 'w') as file:
    # Append three lines to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Read and print the first line
with open(file_path, 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)

# Delete the text file
import os
os.remove(file_path)

print(f"{file_path} has been created, modified, and deleted.")

# done