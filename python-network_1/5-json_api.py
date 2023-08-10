import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if isinstance(json_data, dict) and bool(json_data):
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
