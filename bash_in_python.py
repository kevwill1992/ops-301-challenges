# Script Name:                    Bash in Python
# Author:                         Kevin Williams
# Date of Lastest revision:       12/5/2023
# Purpose:                       Creating a Python script that executes bash commands
# Additional Sources:            https://chat.openai.com/share/14de2cf5-b702-4cfb-9da9-2c649edb2de3
import os

def main():
    # Declare three variables
    user_name = None
    ip_address = None
    hardware_info = None

    try:
        # Execute 'whoami' command
        user_name = os.popen('whoami').read().strip()

        # Execute 'ip a' command
        ip_address = os.popen('ip a').read()

        # Execute 'lshw -short' command
        hardware_info = os.popen('lshw -short').read()

        # Print results using the print() function
        print(f"Current user: {user_name}")
        print("\nIP Address Information:")
        print(ip_address)
        print("\nHardware Information:")
        print(hardware_info)

    except Exception as e:
        # Handle exceptions, if any
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Call the main function
    main()
