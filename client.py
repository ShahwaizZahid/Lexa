import requests
import os

def google_search(query):
    api_key = 'AIzaSyASc1tK0Y_D3ds8uqUgxGYzFzaPD2sj8xQ'
    cse_id = 'd1e5d3d599c2841b7'
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        data = response.json()
        items = data.get('items', [])

        if items:
            first_result = items[0]
            message = f"{first_result.get('snippet')}"
            print(message)
            return message
            # print(f"Link: {first_result.get('link')}")
        else:
            print("No results found.")
    except requests.exceptions.RequestException as e:
        print(f"Error performing Google Search: {e}")

# Example usage
# google_search("What is coding")
