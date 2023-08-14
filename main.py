import json
from modules.server_data import fetch_and_save_server_data
from modules.server_count import get_server_count

API_BASE_URL = 'https://api.cornbread2100.com'

def fetch_data():
    skip = int(input("Enter the number of results to skip: "))
    limit = int(input("Enter the number of results to limit: "))
    fetch_query = {
        "hasFavicon": True
    }
    output_file = 'server_data.json'
    fetch_and_save_server_data(fetch_query, output_file, skip=skip, limit=limit)
    print('Server data fetched and saved.')

def get_count():
    fetch_query = {
        "hasFavicon": True
    }
    server_count = get_server_count(fetch_query)
    print(f'Total number of servers matching the filter criteria: {server_count}')

def main():
    print("1. Fetch and Save Server Data")
    print("2. Get Count of Servers")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        fetch_data()
    elif choice == "2":
        get_count()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
