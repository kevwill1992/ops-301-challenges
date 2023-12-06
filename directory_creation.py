# Script Name:                    Directory Creation
# Author:                         Kevin Williams
# Date of Lastest revision:       12/5/2023
# Purpose:                       Utilizing a function from the os library to generate directory info
# Additional Sources:            https://chat.openai.com/share/607ca348-aa9f-4650-9e71-afba1c549020

#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

def generate_directory_structure(user_path):
    for root, dirs, files in os.walk(user_path):
        # Print the current directory
        print(f"Current Directory: {root}")

        # Print subdirectories
        print("Subdirectories:")
        for dir_name in dirs:
            print(os.path.join(root, dir_name))

        # Print files
        print("Files:")
        for file_name in files:
            print(os.path.join(root, file_name))

        print("-" * 40)

if __name__ == "__main__":
    # Ask user for a file path
    user_path = input("Enter a directory path: ")

    # Validate if the provided path exists
    if os.path.exists(user_path):
        # Call the function to generate and print directory structure
        generate_directory_structure(user_path)
    else:
        print("Error: The provided path does not exist.")



# End