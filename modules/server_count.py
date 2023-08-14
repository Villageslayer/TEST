import requests

API_BASE_URL = 'https://api.cornbread2100.com'

def get_server_count(fetch_query):
    count_response = requests.post(f'{API_BASE_URL}/countServers', json=fetch_query)
    if count_response.status_code == 200:
        count_data = count_response.json()
        count = count_data.get('count', 0)
        return count
    else:
        print('Error fetching count of servers:', count_response.text)
        return 0
