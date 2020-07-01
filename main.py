import requests
from PIL import Image
from io import BytesIO

from keys import *

UNSPLASH_URL = 'https://api.unsplash.com'

def get_image():
    response = requests.get(UNSPLASH_URL + '/photos/random/?client_id=' + UNSPLASH_ACCESS_KEY)

    if response.status_code == 401:
        print('request is not authorized')
    elif response.status_code == 404:
        print('request error')

    image_url = response.json()['urls']['raw']
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image.save('temp.jpg')

get_image()