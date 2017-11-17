import os
import shutil

import requests


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    print(file_name)
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)

def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw
