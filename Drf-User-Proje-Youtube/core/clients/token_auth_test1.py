import requests
from pprint import pprint


# {'key': '2f2a147779931af8e070544b5bd04fa0eb869491'}
def client():

    credentials = {
        "username":"test_user",
        "password":"Yapan78."
    }

    response = requests.post(
        url = "http://127.0.0.1:8000/api/dj_rest_auth/login/",
        data=credentials
    )

    print(response.status_code)

    response_data = response.json()

    pprint(response_data)

if __name__ == "__main__":
    client()