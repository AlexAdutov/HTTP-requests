import requests
from settings import TOKEN

class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        print(path)
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json()['href'])
        return response.json()['href']

    def upload(self, local_path, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        upload_url = self._get_upload_link(file_name)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
             print('Загрузка произошла успешно!')

if __name__ == '__main__':
    path_to_file = "D:/Files/Hello world.txt"
    token='здесь мог быть ваш токен'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, path_to_file)
