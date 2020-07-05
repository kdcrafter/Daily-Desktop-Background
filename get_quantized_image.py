import requests
from PIL import Image
from random import randint
from io import BytesIO

from keys import *
from config import *

BACKGROUND_EXTENSION = 'png' # png to prevent lossy compression
BACKGROUND_FILENAME = 'background.' + BACKGROUND_EXTENSION
BACKGROUND_QUANTIZED_FILENAME = 'background_quantized.' + BACKGROUND_EXTENSION
UNSPLASH_URL = 'https://api.unsplash.com/search/photos/'

def get_image():
    # Get image url response
    image_number = randint(1, MAX_IMAGES)
    response = requests.get(UNSPLASH_URL +
        '?client_id=' + UNSPLASH_ACCESS_KEY + 
        '&query=' + QUERY +
        '&orientation=landscape' +
        '&page=' + str(image_number) +
        '&per_page=1')

    if response.status_code != 200:
        print('Status Code:', response.status_code)
        print(response.json()['errors'])
        quit()
    elif response.json() == {}:
        print('Status Code:', 500)
        print(['Internal Server Error'])
        quit()

    # Get image response
    image_url = response.json()['results'][0]['urls']['raw']
    image_url += ('&fm=' + BACKGROUND_EXTENSION +
        '&w=' + str(WIDTH) +
        '&h=' + str(HEIGHT) +
        '&fit=min')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    return image

if __name__ == '__main__':
    image = get_image()
    image.save(BACKGROUND_FILENAME)

    image = image.quantize(NUMBER_COLORS).convert('RGB')
    image.save(BACKGROUND_QUANTIZED_FILENAME)
