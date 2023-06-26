# Author: https://github.com/Tsprnay
import random
import string

import requests

from func.config import freeimageapi


async def random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))

async def upload_image(image_path):
    url = 'https://freeimage.host/api/1/upload'

    files = {'source': image_path}
    data = {'key': freeimageapi, 'action': 'upload', 'format': 'json'}

    response = requests.post(url, files=files, data=data)
    print(response.json())

    if response.json()["status_code"] == 200:
        print('1')
        return response.json()["image"]["url"]
    else:
        print('2')
        return False
