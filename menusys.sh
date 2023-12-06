#!/bin/bash

# Script Name:                    Conditionals in Menu Systems
# Author:                         Kevin Williams
# Date of Lastest revision:       11/30/2023
# Purpose:                        Creating a script that launches a menu system
# Additional Sources:             https://chat.openai.com/share/a10f3d26-85ee-4af7-bd73-e59147b7c650        

# Declaration of variables

while true; do
    # Display menu
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    
    read -p "Enter your choice (1-4): " choice


    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping self (loopback address)
            ;;
        3)
            ifconfig  # Display network adapter information
            ;;
        4)
            echo "Exiting program. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    echo
done
