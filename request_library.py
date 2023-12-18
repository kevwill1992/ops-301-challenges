# Script Name:                    Python Request 
# Author:                         Kevin Williams
# Date of Lastest revision:       12/12/2023
# Purpose:                        Using psutil to fetch system information
# Additional Sources:            https://chat.openai.com/share/4ba38dda-fbf4-4e5f-bc66-f2302d818fe5


import requests

def get_user_input():
    url = input("Enter the destination URL: ")
    method = input("Choose HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
    return url, method

def print_request_details(url, method):
    print(f"\nRequest details:")
    print(f"URL: {url}")
    print(f"HTTP Method: {method}")

def confirm_request():
    return input("Do you want to proceed with the request? (yes/no): ").lower() == 'yes'

def send_request(url, method):
    try:
        response = requests.request(method, url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def print_response_info(response):
    if response is not None:
        print(f"\nResponse details:")
        print(f"Status Code: {response.status_code} - {requests.status_codes._codes[response.status_code][0]}")
        print("Headers:")
        for header, value in response.headers.items():
            print(f"  {header}: {value}")

def main():
    url, method = get_user_input()
    print_request_details(url, method)

    if confirm_request():
        response = send_request(url, method)
        print_response_info(response)

if __name__ == "__main__":
    main()
