import requests

def fetch_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    except:
        return "Failed to fetch quote."

if __name__ == "__main__":
    print(fetch_random_quote())
