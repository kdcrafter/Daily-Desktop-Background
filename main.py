import requests
from PIL import Image
from io import BytesIO
from random import randint

from keys import *
from config import *

def get_image():
    image_number = randint(1, MAX_IMAGES)

    response = requests.get('https://api.unsplash.com/search/photos/' +
        '?client_id=' + UNSPLASH_ACCESS_KEY + 
        '&query=desktop-background' +
        '&orientation=landscape' +
        '&page=' + str(image_number) +
        '&per_page=1')

    if response.status_code != 200:
        print('Status Code:', response.status_code)
        print(response.json()['errors'])
        return
    elif response.json() == {}:
        print('Status Code:', 500)
        print(['Internal Server Error'])
        return

    image_url = response.json()['results'][0]['urls']['raw']
    image_url += ('&q=' + str(COMPRESSION_QUALITY) +
        '&fm=jpg' +
        '&w=' + str(WIDTH) +
        '&h=' + str(HEIGHT) +
        '&fit=min')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image.save('temp.jpg')

get_image()