# Script Name:                    Conditional Statements
# Author:                         Kevin Williams
# Date of Lastest revision:       12/7/2023
# Purpose:                       Creating if statements using logical conditionals
# Additional Sources:           https://chat.openai.com/share/b25761a5-bedd-4c48-a5e6-c873fc45dee0

# Assume we have a variable 'number'
number = 42

# Check if the number is less than 0
if number < 0:
    print("The number is negative")

# Check if the number is equal to 0
elif number == 0:
    print("The number is zero")

# Check if the number is between 1 and 10 (inclusive)
elif 1 <= number <= 10:
    print("The number is between 1 and 10")

# Check if the number is between 11 and 20 (inclusive)
elif 11 <= number <= 20:
    print("The number is between 11 and 20")

# Check if the number is greater than 20
elif number > 20:
    print("The number is greater than 20")

# If none of the above conditions are met
else:
    print("The number is in an unspecified range")

# done 