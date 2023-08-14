# Cornbreads Mc Server Api DOCS

This README provides a list of possible filters that can be used with the MC Server API to query servers based on various criteria.

## API Endpoint

The Server API allows you to query servers based on different filters. The base URL for the API is:

https://api.cornbread2100.com


You can add the `skip` and `limit` query parameters to the API endpoint to skip forward in the results list and limit the amount of data retrieved. For example:

- To skip the first 10 results and retrieve the next 20 results:

https://api.cornbread2100.com/servers?skip=10&limit=20


## Counting Servers

To get the count of servers that match the filter criteria without fetching the entire server list, you can use the `/countServers` endpoint. For example:

- To count the servers that match a specific filter:
https://api.cornbread2100.com/countServers?geo.country=US&players.online={$gte:10}

## Filters

1. **Country Filter**:
   - Filter: `"geo.country": "US"`
   - Description: Replace `"US"` with the desired 2-letter country code.

2. **Online Players Filter**:
   - Filter: `"players.online": "2"`
   - Description: Replace `"2"` with the desired number of online players.

3. **Minimum Online Players Filter**:
   - Filter: `"players.online": { "$gte": 10 }`
   - Description: Replace `10` with the desired minimum number of online players.

4. **Maximum Online Players Filter**:
   - Filter: `"players.online": { "$lte": 50 }`
   - Description: Replace `50` with the desired maximum number of online players.

5. **Player Cap Filter**:
   - Filter: `"players.max": 100`
   - Description: Replace `100` with the desired player cap.

6. **Is Full Filter**:
   - Filter (Server is full): `"players.online": { "$eq": "$players.max" }`
   - Filter (Server is not full): `"players.online": { "$ne": "$players.max" }`

7. **Version Filter**:
   - Filter: `"version.name": { "$regex": "1.16" }`
   - Description: Replace `"1.16"` with the desired version.

8. **Has Image Filter**:
   - Filter: `"hasFavicon": true`
   - Description: Server has an image.

9. **Description Filter**:
   - Filter: `"description": { "$regex": "awesome server", "$options": "i" }`
   - Description: Replace `"awesome server"` with the desired description.

10. **Player Name Filter**:
    - Filter: `"players.sample": { "$elemMatch": { "name": "PlayerName" } }`
    - Description: Replace `"PlayerName"` with the desired player name.

11. **Has Player List Filter**:
    - Filter: `"players.sample": { "$exists": true }` (Server has a player list)
    - Filter: `"players.sample": { "$not": { "$size": 0 } }` (Player list is not empty)

12. **Last Seen Filter**:
    - Filter: `"lastSeen": { "$gte": ISODate("2023-01-01T00:00:00Z") }`
    - Description: Replace date with the desired last seen date.

13. **IP Range Filter**:
    - Filter: `"ip": { "$regex": "^192\\.168\\.1\\.", "$options": "i" }`
    - Description: Replace `"192\\.168\\.1\\."` with the desired IP range.

14. **Organization Filter**:
    - Filter: `"org": "OrgName"`
    - Description: Replace `"OrgName"` with the desired organization.

## Usage

To use these filters with the API, construct JSON queries by including the desired filter criteria. Replace the placeholder values with your specific requirements.

Example usage in Python:

```python
import requests

API_BASE_URL = 'https://api.cornbread2100.com'

# Example query using filters and skip/limit
skip_amount = 10  # Number of results to skip
limit_amount = 20  # Number of results to limit

fetch_query = {
    "geo.country": "US",
    "players.online": { "$gte": 10 }
}

server_response = requests.post(f'{API_BASE_URL}/servers?skip={skip_amount}&limit={limit_amount}', json=fetch_query)

if server_response.status_code == 200:
    server_data = server_response.json()
    if server_data:
        for server in server_data:
            print('Server Data:', server)
    else:
        print('No servers found.')
else:
    print('Error fetching server data:', server_response.text)
