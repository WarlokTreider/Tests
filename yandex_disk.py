import requests


class YandexDisk:
    base_url = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, token):
        self.token = token

    def create_folder(self, path):
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        params = {
            "path": path
        }
        response = requests.put(self.base_url, headers=headers, params=params)
        return response

    def get_folder(self, path):
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        params = {
            "path": path
        }
        response = requests.get(self.base_url, headers=headers, params=params)
        return response

    def delete_folder(self, path):
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        params = {
            "path": path,
            "permanently": "true"
        }
        response = requests.delete(self.base_url, headers=headers, params=params)
        return response
