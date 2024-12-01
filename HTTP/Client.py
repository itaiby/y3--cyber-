import requests

def main():
    url = ("http://localhost:8000/sum")
    params = {
        "a": 6,
        "b": 1,
        "c": 4,
        "d": 9,
        "f": 3,
        "e": 7,
    }

    try:
        response = requests.get(url, params=params)
        print("Request sent.")
        print(f"URL: {response.url}")
        print("Response received:")
        print(response.status_code ,response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()