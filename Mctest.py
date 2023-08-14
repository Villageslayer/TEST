import json
from modules.server_data import fetch_and_save_server_data
from modules.server_count import get_server_count

API_BASE_URL = 'https://api.cornbread2100.com'

fetch_query = {
    "hasFavicon": True
}

output_file = 'server_data.json'

# Fetch and save server data
fetch_and_save_server_data(fetch_query, output_file)

# Fetch and print count of servers
server_count = get_server_count(fetch_query)
print(f'Total number of servers matching the filter criteria: {server_count}')
