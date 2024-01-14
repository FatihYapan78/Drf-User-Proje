import requests
from pprint import pprint

def client():

    credentials = {
        "username":"test_user8",
        "email": "testuser@test.co",
        "password1":"Yapan78.",
        "password2":"Yapan78.",
    }

    response = requests.post(
        url = "http://127.0.0.1:8000/api/dj_rest_auth/registration/",
        data=credentials
    )

    if response.status_code == 204:
        print("Kullanıcı Kaydı Başarılı")
    else:
        print(f'Hata Oluştu. {response.status_code}')
        print(response.json())

if __name__ == "__main__":
    client()