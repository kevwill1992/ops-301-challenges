#!/bin/bash

# Script Name:                    Append
# Author:                         Kevin Williams
# Date of Lastest revision:       11/28/2023
# Purpose:                        Apply today's date to a log file
# Additional Sources:             https://chat.openai.com/share/bc16923e-011d-4880-83dc-8ccf1ff5e161      

# Declaration of variables
source_file="/var/log/syslog"
current_date=$(date +"%Y%m%d_%H%M%S")
destination_file="syslog_backup_${current_date}.log"

cp "$source_file" "$destination_file"

echo "Backup completed. File saved as: $destination_file"

# End