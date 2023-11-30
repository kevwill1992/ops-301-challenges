#!/bin/bash

# Script Name:                    File Permissions
# Author:                         Kevin Williams
# Date of Lastest revision:       11/29/2023
# Purpose:                        Altering file permissions
# Execution:                      filepermissions.sh  
# Additional Sources:             https://chat.openai.com/share/21d7ba83-bb85-47db-8cf0-d84435049556      

# Declaration of variables

read -p "Enter the directory path: " directory_path
read -p "Enter the permissions number (e.g., 777): " permissions

chmod -R "$permissions" "$directory_path"

echo -e "\nDirectory contents and neew permissions settings:'
ls -l "$directory_path"

echo -3 "\nPermissions change completed for files in $directory_path."

# End