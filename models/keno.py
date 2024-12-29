import requests
from requests.auth import HTTPDigestAuth
from requests import session

class CameraSettingsAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.headers = {'User-Agent':'curl/4.5.6'}
        self.session.auth = requests.auth.HTTPDigestAuth(self.username, self.password)
        #self.session.headers.update({'User -Agent': 'curl/4.5.6'})

    def get_device_para(self):
        url = f"{self.base_url}/digest/frmDevicePara"
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Проверка на наличие ошибок HTTP
            return response.json()  # Возвращаем JSON-ответ
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def get_device_time(self):
        url = f"{self.base_url}/digest/frmDeviceTimeCtrl"
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Проверка на наличие ошибок HTTP
            return response.json()  # Возвращаем JSON-ответ
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def get_network_settings(self):
        url = f"{self.base_url}/digest/frmNetworkSettings"
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Проверка на наличие ошибок HTTP
            return response.json()  # Возвращаем JSON-ответ
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

