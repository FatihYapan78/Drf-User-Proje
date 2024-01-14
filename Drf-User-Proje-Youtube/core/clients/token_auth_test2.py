import requests
from pprint import pprint


# {'key': '2f2a147779931af8e070544b5bd04fa0eb869491'}
def client():
    token = 'Token 2f2a147779931af8e070544b5bd04fa0eb869491'
    headers = {
        "Authorization": token,
    }
    response = requests.get(
        url = "http://127.0.0.1:8000/api/profiller/",
        headers= headers
    )

    print(response.status_code)

    response_data = response.json()

    pprint(response_data)

if __name__ == "__main__":
    client()