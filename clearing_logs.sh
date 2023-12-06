#!/bin/bash

# Script Name:                    Clearing Logs
# Author:                         Kevin Williams
# Date of Lastest revision:       12/5/2023
# Purpose:                        Clearing Logs
# Additional Sources:             https://chat.openai.com/share/21d7ba83-bb85-47db-8cf0-d84435049556      

# Declaration of variables

# Function to print file size
print_file_size() {
  echo "File Size of $1: $(du -h "$1" | cut -f1)"
}

# Backup directory
backup_dir="/var/log/backups"

# Create backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Get current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Log files to compress
log_files=("/var/log/syslog" "/var/log/wtmp")

# Perform tasks for each log file
for file in "${log_files[@]}"; do
  # Print original file size
  print_file_size "$file"

  # Compress the log file to backup directory
  compressed_file="$backup_dir/$(basename "$file")-$timestamp.zip"
  gzip -c "$file" > "$compressed_file"

  # Clear the contents of the original log file
  echo -n > "$file"

  # Print compressed file size
  print_file_size "$compressed_file"

  # Compare sizes
  original_size=$(du -b "$file" | cut -f1)
  compressed_size=$(du -b "$compressed_file" | cut -f1)
  echo "Size comparison:"
  echo "Original: $original_size bytes"
  echo "Compressed: $compressed_size bytes"

done
