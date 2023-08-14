import requests
import json

API_BASE_URL = 'https://api.cornbread2100.com'

def fetch_and_save_server_data(fetch_query, output_file, skip=None, limit=None):
    params = {}
    if skip is not None:
        params['skip'] = skip
    if limit is not None:
        params['limit'] = limit

    server_response = requests.post(f'{API_BASE_URL}/servers', json=fetch_query, params=params)
    if server_response.status_code == 200:
        server_data = server_response.json()
        if server_data:
            server = server_data if isinstance(server_data, list) else server_data
            with open(output_file, 'w') as file:
                json.dump(server, file, indent=4)
            print(f'Server Data saved to {output_file}')
        else:
            print('No servers found.')
    else:
        print('Error fetching server data:', server_response.text)
