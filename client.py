import requests
import os
from dotenv import load_dotenv

load_dotenv()

def google_search(query):
    api_key = os.getenv('api_key')
    cse_id = os.getenv('cse_id')
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
